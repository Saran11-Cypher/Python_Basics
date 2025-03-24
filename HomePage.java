package TestNG;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import org.openqa.selenium.JavascriptExecutor;

public class HomePage {
    WebDriver driver;
    WebDriverWait wait;

    public HomePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void openFlightsTab() {
        try {
            // Close any popups if present
            closePopup();

            // Wait for and click Flights tab
            WebElement flightsTab = wait.until(ExpectedConditions.elementToBeClickable(
                By.xpath("//a[@class='makeFlex hrtlCenter column' and @href='/flights/']")
            ));
            flightsTab.click();

        } catch (Exception e) {
            System.out.println("Flights tab not found or already open.");
        }
    }

    public void closePopup() {
        try {
            WebElement closePopup = wait.until(ExpectedConditions.presenceOfElementLocated(
                By.xpath("//span[@class='commonModal__close']")
            ));

            // 🔹 Scroll into view
            ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", closePopup);

            // 🔹 Use JavaScript Click (prevents interception)
            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", closePopup);

            System.out.println("Popup closed.");
            Thread.sleep(2000);  // 🔹 Allow time for UI to update
        } catch (Exception e) {
            System.out.println("No popup found or already closed.");
        }
    }

    public void selectRoundTrip() {
        WebElement roundTrip = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//li[text()='Round Trip']")
        ));
        roundTrip.click();
    }
}
