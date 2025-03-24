package TestNG;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import java.util.List;
import org.openqa.selenium.JavascriptExecutor;

public class FlightsPage {
    WebDriver driver;
    WebDriverWait wait;

    public FlightsPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void enterFromCity(String from) {
        WebElement fromField = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//label[@for='fromCity']")
        ));
        fromField.click();

        WebElement fromInput = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//input[@placeholder='From']")
        ));
        fromInput.sendKeys(from);

        // Select the first suggestion
        WebElement firstSuggestion = wait.until(ExpectedConditions.elementToBeClickable(
        		By.xpath("//div[@role='listbox']//ul//li[@role='option']//p[contains(text(), '" + from + "')]")

        ));
        firstSuggestion.click();
    }

    public void enterToCity(String to) {
        WebElement toInput = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//input[@id='toCity']")
        ));
        toInput.click();
        toInput.sendKeys(to);

        // Wait for the dropdown list to appear
        WebElement toOption = wait.until(ExpectedConditions.elementToBeClickable(
        		By.xpath("//div[@role='listbox']//ul//li[@role='option']//p[contains(text(), '" + to + "')]")
        ));
        toOption.click();
    }
    public void selectDates() {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        // 🔹 Wait until the departure label is visible and clickable
        WebElement dateField = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//label[@for='departure']")
        ));

        // 🔹 Scroll into view (optional, but useful)
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", dateField);

        // 🔹 Click using JavaScript to bypass overlays
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", dateField);

        System.out.println("✅ Departure date field clicked successfully.");
        // 🔹 Wait for and select the departure date
        WebElement departureDate = wait.until(ExpectedConditions.elementToBeClickable(
        		By.xpath("//div[@aria-label= 'Wed Mar 26 2025']")
        ));
        departureDate.click();

        // 🔹 Select the return date (for round trip)
        WebElement returnDate = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//div[@aria-label= 'Wed Apr 02 2025']")
        ));
        returnDate.click();
    }
    public void selectTravellerClass() {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            // 🔹 Handle potential popups before interacting
            closeOverlays();
            
            // 🔹 Click on the Traveller & Class field
            WebElement travellerClassField = wait.until(ExpectedConditions.elementToBeClickable(
                By.xpath("//label[@for='travellers']")
            ));
            
            // Use JavaScript Click as a fallback
            try {
                travellerClassField.click();
            } catch (Exception e) {
                ((JavascriptExecutor) driver).executeScript("arguments[0].click();", travellerClassField);
            }

            // 🔹 Select number of Adults (Modify as needed)
            WebElement adultCount = wait.until(ExpectedConditions.elementToBeClickable(
                By.xpath("//li[@data-cy='adults-1']")
            ));
            adultCount.click();

            // 🔹 Click 'Apply' button
            WebElement applyButton = wait.until(ExpectedConditions.elementToBeClickable(
                By.xpath("//button[text()='APPLY']")
            ));
            applyButton.click();

            System.out.println("✅ Traveller class selected successfully.");

        } catch (Exception e) {
            System.out.println("❌ Error selecting traveller class: " + e.getMessage());
        }
    }

    /**
     * Handles overlays or popups that may block elements.
     */
    private void closeOverlays() {
        try {
            List<WebElement> overlays = driver.findElements(By.xpath("//div[contains(@class,'overlay')]"));
            for (WebElement overlay : overlays) {
                ((JavascriptExecutor) driver).executeScript("arguments[0].style.display='none';", overlay);
            }
            System.out.println("✅ Overlays closed successfully.");
        } catch (Exception e) {
            System.out.println("⚠ No overlays found.");
        }
    }

    public void searchFlights() {
        // 🔹 Click on the Search button
    	WebElement searchButton = wait.until(ExpectedConditions.elementToBeClickable(
    		    By.xpath("//a[text()='Search']")
    		));
    		((JavascriptExecutor) driver).executeScript("arguments[0].click();", searchButton);

        // 🔹 Wait until flight results load
    	WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
    	wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[contains(@class, 'listingCard')]")));
    }
    public void printSpiceJetFlights() {
        // 🔹 Wait until flights are visible
        wait.until(ExpectedConditions.presenceOfElementLocated(
            By.xpath("//div[contains(@class, 'listingCard')]")
        ));

        // 🔹 Get all flight cards
        List<WebElement> flights = driver.findElements(By.xpath("//div[contains(@class, 'listingCard')]"));

        boolean found = false;
        for (WebElement flight : flights) {
            // 🔹 Check if SpiceJet is in the airline name
            WebElement airlineName = flight.findElement(By.xpath(".//span[contains(text(), 'SpiceJet')]"));
            if (airlineName.isDisplayed()) {
                found = true;
                System.out.println("SpiceJet Flight Found: " + flight.getText());
            }
        }

        if (!found) {
            System.out.println("No SpiceJet flights available.");
        }
    }


}
