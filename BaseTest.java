package TestNG;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.openqa.selenium.chrome.ChromeOptions;
//import io.github.bonigarcia.wdm.WebDriverManager;
public class BaseTest {
	protected WebDriver driver;
	
	
	  @BeforeClass
	    public void setUp() {
	       // WebDriverManager.chromedriver().setup();
		  ChromeOptions options = new ChromeOptions();
		  options.setExperimentalOption("excludeSwitches", new String[]{"enable-automation"});
		  options.setExperimentalOption("useAutomationExtension", false);
	      driver = new ChromeDriver();
	      driver.manage().window().maximize();
	      driver.get("https://www.makemytrip.com/");
	    }
	  @AfterClass
	    public void tearDown() {
	        if (driver != null) {
	            driver.quit();
	        }
	    }
}
