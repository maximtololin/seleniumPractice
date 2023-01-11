import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from defGlobal import handle_input, handle_click, open_link_Firefox

links = ["https://web.dev.slaver.vip/#/pages/dashboard",
         "https://web.dev.slaver.vip/#/pages/1_team/workers",
         "https://web.dev.slaver.vip/#/pages/1_team/positions",
         "https://web.dev.slaver.vip/#/pages/1_team/payouts",
         "https://web.dev.slaver.vip/#/pages/1_team/payroll",
         "https://web.dev.slaver.vip/#/pages/1_team/cardAccess",
         "https://web.dev.slaver.vip/#/pages/2_botPlatform/bots",
         "https://web.dev.slaver.vip/#/pages/2_botPlatform/channels",
         "https://web.dev.slaver.vip/#/pages/2_botPlatform/content",
         "https://web.dev.slaver.vip/#/pages/2_botPlatform/analytics",
         "https://web.dev.slaver.vip/#/pages/2_botPlatform/mailings",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/gram",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/responsible",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/analytics",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/dialogflow",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/messenger",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/credentials",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/crypto",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/affiliate",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/screenSoft",
         "https://web.dev.slaver.vip/#/pages/3_dialogs/credentials",
         "https://web.dev.slaver.vip/#/pages/4_analytics/bot",
         "https://web.dev.slaver.vip/#/pages/4_analytics/pm",
         "https://web.dev.slaver.vip/#/pages/5_management/marketing/marketing",
         "https://web.dev.slaver.vip/#/pages/5_management/sales/sales",
         "https://web.dev.slaver.vip/#/pages/5_management/tv/tv",
         "https://web.dev.slaver.vip/#/pages/6_assignment/mainScreen",
         "https://web.dev.slaver.vip/#/pages/project/settings",
         "https://web.dev.slaver.vip/#/pages/auth/login",
         "https://web.dev.slaver.vip/#/pages/auth/forgot-password",
         "https://web.dev.slaver.vip/#/pages/auth/new-password",
         "https://web.dev.slaver.vip/#/pages/auth/register",
         "https://web.dev.slaver.vip/#/pages/auth/lockscreen",
         "https://web.dev.slaver.vip/#/pages/auth/404",
         "https://web.dev.slaver.vip/#/pages/auth/500",
         "https://web.dev.slaver.vip/#/pages/auth/project",
         "https://web.dev.slaver.vip/#/pages/auth/register",
         "https://web.dev.slaver.vip/#/pages/project/settings",
         "https://web.dev.slaver.vip/#/pages/service/massDelete",
         "https://web.dev.slaver.vip/#/pages/service/crypto",
         "https://web.dev.slaver.vip/#/pages/hallFame",
         "https://web.dev.slaver.vip/#/pages/tv",
         "https://web.dev.slaver.vip/#/pages/demo/saleSplashDemo",
         "https://web.dev.slaver.vip/#/pages/telegramWebApps/buyerRequest",
         "https://web.dev.slaver.vip/#/pages/7_botAnalytics", ]

email = "r20-maksim@monowork.pro"
password = "Cwajxy4RWQ!"
login_link = "https://web.dev.slaver.vip/#/auth/login"


def auth_login():
    driver = open_link_Firefox(login_link)
    handle_input(By.ID, "email", email)
    handle_input(By.ID, "password", password)
    handle_click(By.TAG_NAME, "button")

    driver.quit()


auth_login()
