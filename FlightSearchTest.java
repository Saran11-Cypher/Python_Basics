package TestNG;

import org.testng.annotations.Test;
import org.testng.annotations.DataProvider;

public class FlightSearchTest extends BaseTest {

    @Test(dataProvider = "flightData")
    public void searchAndPrintSpiceJet(String from, String to) throws InterruptedException {
        driver.get("https://www.makemytrip.com/");

        HomePage homePage = new HomePage(driver);
        FlightsPage flightsPage = new FlightsPage(driver);
        
        homePage.closePopup();
        
        homePage.openFlightsTab();
        homePage.selectRoundTrip();
        flightsPage.enterFromCity(from);
        flightsPage.enterToCity(to);
        flightsPage.selectDates();
        flightsPage.selectTravellerClass();
        flightsPage.searchFlights();
        flightsPage.printSpiceJetFlights();
    }

    @DataProvider(name = "flightData")
    public Object[][] getFlightData() {
        return new Object[][] {
            {"New Delhi", "Mumbai"},
            {"Bengaluru", "Chennai"}
        };
    }
}
