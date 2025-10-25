# form_filler_by_label.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback

FORM_URL = "https://forms.gle/WT68aV5UnPajeoSc8"
OUTPUT_SCREENSHOT = "confirmation.png"

# The values you want to fill (use the exact label texts if they differ, update keys)
VALUES = {
    "Full Name": "K.R.S.S Manikanta",
    "Contact Number": "6303666259",
    "Email ID": "kesireddynandu004@gmail.com",
    "Full Address": "Flat 203, Golden Maple Residences, Sri Balaji Layout, Gajularamaram, Hyderabad, Telangana",
    "Pin Code": "500055",
    "Date of Birth": "15-10-2004",  # we'll try multiple formats if needed
    "Gender": "Male",
    # Do NOT include CAPTCHA key here
}

def find_label_text(container):
    """Try several ways to extract the question label text from the question container."""
    # Common Google Forms label containers (may change across forms)
    selectors = [
        ".//div[contains(@class,'freebirdFormviewerComponentsQuestionBaseTitle')]",  # common
        ".//div[contains(@class,'uArJ5e')]",  # fallback class seen in some forms
        ".//div[@role='heading']",
        ".//span[contains(@class,'freebirdFormviewerComponentsQuestionBaseTitle')]",
    ]
    for sel in selectors:
        try:
            el = container.find_element(By.XPATH, sel)
            text = el.text.strip()
            if text:
                return text
        except:
            pass
    # last resort: all text inside container
    try:
        return container.text.strip().split("\n")[0]
    except:
        return ""

def fill_input(elem, value):
    try:
        elem.clear()
    except:
        pass
    try:
        elem.send_keys(value)
        return True
    except Exception:
        return False

def try_fill_date_input(elem, date_value):
    """Try a few common date formats into a date input."""
    candidates = [date_value, date_value.replace("-", "/"), date_value.replace("-", "."),
                  "/".join(reversed(date_value.split("-"))) if "-" in date_value else date_value]
    for c in candidates:
        try:
            elem.clear()
        except:
            pass
        try:
            elem.send_keys(c)
            return True
        except:
            continue
    return False

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # avoid headless if manual captcha input required
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(FORM_URL)
    time.sleep(3)  # let form load fully

    # Google forms usually wrap questions in a container; try several possible containers
    question_containers = []
    possible_xpaths = [
        "//div[@role='listitem']",  # common
        "//div[contains(@class,'freebirdFormviewerViewItemsItemItem')]", 
        "//div[contains(@class,'freebirdFormviewerViewItemsItem')]"
    ]
    for xp in possible_xpaths:
        try:
            els = driver.find_elements(By.XPATH, xp)
            if els:
                question_containers = els
                break
        except Exception:
            pass

    if not question_containers:
        print("⚠️ Could not find question containers. Inspect the form and adjust selectors.")
        return

    print(f"Found {len(question_containers)} question containers. Parsing...")

    # iterate containers and fill based on label
    for idx, cont in enumerate(question_containers):
        try:
            label = find_label_text(cont)
            print(f"\nQuestion #{idx+1} label detected: '{label}'")
            # Normalize label (strip star and whitespace)
            label_key = label.replace("*", "").strip()

            # Skip captcha-like labels (they often contain 'Type this code' or 'This code is to verify')
            if "Type this code" in label or "verify" in label.lower() or "captcha" in label.lower():
                print(" - Detected CAPTCHA / verification field — leaving for manual entry.")
                continue

            # try to find input or textarea inside container
            try:
                input_el = cont.find_element(By.CSS_SELECTOR, "input")
            except:
                input_el = None
            try:
                textarea_el = cont.find_element(By.CSS_SELECTOR, "textarea")
            except:
                textarea_el = None

            # some date fields may be broken into multiple inputs — try to find input[type='date'] or .quantumWizDatepickerInput
            date_el = None
            try:
                date_el = cont.find_element(By.CSS_SELECTOR, "input[type='date'], input.quantumWizDatepickerInput")
            except:
                date_el = None

            # If label matches key in VALUES (best case)
            if label_key in VALUES:
                val = VALUES[label_key]
                if textarea_el:
                    ok = fill_input(textarea_el, val)
                    print(f" - Filled textarea for '{label_key}': {ok}")
                elif date_el:
                    ok = try_fill_date_input(date_el, val)
                    print(f" - Filled date field for '{label_key}': {ok}")
                elif input_el:
                    ok = fill_input(input_el, val)
                    print(f" - Filled input for '{label_key}': {ok}")
                else:
                    # Try to find any input descendant
                    try:
                        gen_input = cont.find_element(By.XPATH, ".//input|.//textarea")
                        ok = fill_input(gen_input, val)
                        print(f" - Filled generic field for '{label_key}': {ok}")
                    except Exception:
                        print(f" - No fillable input found in container for '{label_key}'.")
            else:
                # Not in VALUES: try to auto-fill if there is a placeholder or small label matching keywords
                lower = label_key.lower()
                if "address" in lower and textarea_el:
                    fill_input(textarea_el, VALUES.get("Full Address", ""))
                    print(" - Auto-filled Address")
                elif "pin" in lower or "pincode" in lower or "pin code" in lower:
                    if input_el:
                        fill_input(input_el, VALUES.get("Pin Code", ""))
                        print(" - Auto-filled Pin Code")
                elif "date" in lower and (date_el or input_el):
                    target = date_el or input_el
                    ok = try_fill_date_input(target, VALUES.get("Date of Birth", ""))
                    print(f" - Auto-filled Date: {ok}")
                elif "gender" in lower and input_el:
                    fill_input(input_el, VALUES.get("Gender", ""))
                    print(" - Auto-filled Gender")
                else:
                    print(" - No matching key for this question; skipping.")

        except Exception as e:
            print("Exception while handling container:", e)
            traceback.print_exc()

    # All automatic fills attempted. Now handle captcha manually
    print("\nAll autos fills done. IMPORTANT: You must enter the verification/CAPTCHA code shown on the form manually in the browser.")
    print("Type the exact code (match letters/numbers exactly, no extra spaces). After typing it, click Submit immediately or press ENTER here to let script click Submit for you.")
    input("➡️ Once you have typed the CAPTCHA in the form, press ENTER here to continue and submit...")

    # Submit attempt
    try:
        submit_button = driver.find_element(By.XPATH, "//div[@role='button' and (contains(., 'Submit') or contains(., 'Submit form') or contains(., 'submit'))]")
        submit_button.click()
        print("Clicked the submit button.")
    except Exception:
        print("Could not find/press submit button automatically. Please press it manually in the browser now.")
        input("Press ENTER after you submit the form manually...")

    time.sleep(2)
    driver.save_screenshot(OUTPUT_SCREENSHOT)
    driver.quit()
    print(f"✅ Screenshot saved as {OUTPUT_SCREENSHOT}")

if __name__ == "__main__":
    main()
