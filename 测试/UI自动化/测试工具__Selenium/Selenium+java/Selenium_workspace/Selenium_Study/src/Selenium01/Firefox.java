package Selenium01;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
 
public class Firefox {
 
    public static void main(String[] args) {
        //System.setProperty("webdriver.firefox.bin", "E:\\InstallSoftWare\\Mozilla Firefox\\firefox.exe");
       // System.setProperty("webdriver.chrome.driver", "D:\\jar\\seleniumjar\\chromedriver_win32\\chromedriver.exe");
        //System.setProperty("webdriver.firefox.marionette","E:\\InstallSoftWare\\Mozilla Firefox\\geckodriver.exe");
        //driver = new ChromeDriver();
        System.out.println("aaaaa");

        WebDriver driver = new FirefoxDriver(); 
        
        System.out.println("bbbb");
        driver.get("https://www.baidu.com/");
        driver.manage().window().maximize();
    }
}