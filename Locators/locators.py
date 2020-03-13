class Locators:
    #loginPage Objects
    email_textbox_css = "input[type='email']"
    password_textbox_css = "input[type='password']"
    email_buttonNext_id = "identifierNext"
    password_buttonNext_id = "passwordNext"


    #homePage Objects
    login_link_text ="Login"
    #username_text_path="//a[@qa='userAccount']/span[@class='ng-binding']"

    gplus_link_css = "a[class*='gplusBtn']"
    search_textbox_id="input"
    search_button_css="button[qa='searchBtn']"

    #common Objects
    basket_link_xpath = "//a[@qa='myBasket']"

    #searchResultPage Objects
    search_products_xpath = "//div[@qa='product']"
    #search_products_xpath = "//div[@qa='product_name']"
    add_selected_product_in_cart=".//button[@qa='add']"

    add_product_name_xpath= ".//div/div/div/a"
    #add_product_name_xpath=".//div//div[@qa='product_name']"
    #// div[ @ qa = 'product'] // div // div[ @ qa = 'product_name']
    #add_product_name_xpath="//div[@qa='product_name']"
    #add_product_name_xpath=".//div[@qa='product_name']"

    #// div[ @ qa = 'product'] // div / div / div / a
    #cartPage Objects
    view_cart_xpath="//button[@qa='viewBasketMB']"
    LOGIN_link_text = "LOGIN"
    view_products_added = "//div[@class='uiv2-yourbasketitems-gridlist']/div/ul/li[2]/a[2]"
    remove_added_products_from_cart_cross_xpath="//a[@qa= 'prodRemove']"