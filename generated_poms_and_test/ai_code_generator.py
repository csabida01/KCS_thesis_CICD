from openai import OpenAI
import time
import re

API_key = ("sk-proj-OVCMiubkgIypmP7iZKyj9pBYY8QuG2uLII7YwSeKa8ZqQg0SEoSjDAm4_MnX_9IA4IT4UMnp-cT3BlbkFJvn"
           "-Ef1BNWz7FhD248o4H5vaQc_lHf4IUQjn_ndFEFfkm3JE3WKY4t4q-GhPVjhDx_t9d95inMA")
ASSISTANT_ID = ("asst_fHZUNHtCyg7kG0k3gJj33mQQ")
client = OpenAI(api_key=API_key)
full_html = """
--Login Header--
URL: https://automationteststore.com/

<div class="navbar-right headerstrip_blocks">
	  	    <div class="block_1"></div>
	  	    <div class="block_2"><div id="customernav" class="navbar">
	<ul class="nav navbar-nav main_menu" id="customer_menu_top">
		<li><a href="https://automationteststore.com/index.php?rt=account/login">Login or register</a></li>
	</ul>
</div></div>
	  	    <div class="block_3"><div class="topnavbar navbar" id="topnav">
	<span class="sr-only">Main Menu</span>
 	<ul id="main_menu_top" class="nav navbar-nav main_menu">
		    	    <li data-id="menu_specials" class="dropdown "><a class="top menu_specials" href="https://automationteststore.com/index.php?rt=product/special"><i class="fa fa-tag"></i>&nbsp;<span class="menu_text">Specials</span></a></li>
<li data-id="menu_account" class="dropdown "><a class="top menu_account" href="https://automationteststore.com/index.php?rt=account/account"><i class="fa fa-user"></i>&nbsp;<span class="menu_text">Account</span></a>
<ul class="sub_menu dropdown-menu">
<li data-id="menu_login" class="dropdown "><a class="sub menu_login" href="https://automationteststore.com/index.php?rt=account/login"><i class="fa fa-user"></i>&nbsp;<span class="menu_text">Login</span></a></li>
<li data-id="menu_order" class="dropdown "><a class="sub menu_order" href="https://automationteststore.com/index.php?rt=account/invoice"><i class="fa fa-briefcase"></i>&nbsp;<span class="menu_text">Check Your Order</span></a></li>
</ul>
</li>
<li data-id="menu_cart" class="dropdown "><a class="top nobackground" href="https://automationteststore.com/index.php?rt=checkout/cart"><i class="fa fa-shopping-cart"></i>&nbsp;<span class="menu_text">Cart</span></a></li>
<li data-id="menu_checkout" class="dropdown "><a class="top menu_checkout" href="https://automationteststore.com/index.php?rt=checkout/shipping"><i class="fa fa-money"></i>&nbsp;<span class="menu_text">Checkout</span></a></li>
	</ul>
<select class="form-control"><option selected="selected" value="">Main Menu</option><option value="https://automationteststore.com/index.php?rt=product/special">&nbsp;Specials</option><option value="https://automationteststore.com/index.php?rt=account/account">&nbsp;Account</option><option value="https://automationteststore.com/index.php?rt=account/login">&nbsp;Login</option><option value="https://automationteststore.com/index.php?rt=account/invoice">&nbsp;Check Your Order</option><option value="https://automationteststore.com/index.php?rt=checkout/cart">&nbsp;Cart</option><option value="https://automationteststore.com/index.php?rt=checkout/shipping">&nbsp;Checkout</option></select></div></div>
	  	    <div class="block_4"><form id="search_form" class="form-search top-search">
    <input type="hidden" name="filter_category_id" id="filter_category_id" value="0">
    <div class="btn-group search-bar">
    	<input type="text" id="filter_keyword" name="filter_keyword" autocomplete="off" class="pull-left input-medium search-query dropdown-toggle" placeholder="Search Keywords" value="" data-toggle="dropdown">
    	 <div class="button-in-search" title="Go"><i class="fa fa-search"></i></div>
        	<ul id="search-category" class="dropdown dropdown-menu col-md-2 noclose">
    		<li class="active"><a id="category_selected">All Categories</a></li>
    		<li class="divider"></li>
    		    			<li class="search-category">
				    <a id="category_0">All Categories</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_68">Apparel &amp; accessories</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_36">Makeup</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_43">Skincare</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_49">Fragrance</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_58">Men</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_52">Hair Care</a>
			    </li>
    		    			<li class="search-category">
				    <a id="category_65">Books</a>
			    </li>
    		    	</ul>
        </div>
</form></div>
	  	</div>

--login box with error--
URL: https://automationteststore.com/index.php?rt=account/login

<fieldset>
				<div class="form-group">
				  <label class="control-label col-sm-4">
				  Login Name:				  </label>
				  <div class="input-group col-sm-5">
					<input type="text" name="loginname" id="loginFrm_loginname" value="" placeholder="" class="form-control ">
				  </div>
				</div>
				<div class="form-group">
				  <label class="control-label col-sm-4">Password:</label>
				  <div class="input-group col-sm-5">
					<input type="password" name="password" id="loginFrm_password" value="" placeholder="" class="form-control ">
				  </div>
				</div>
				<a href="https://automationteststore.com/index.php?rt=account/forgotten/password">Forgot your password?</a>
								&nbsp;&nbsp;<a href="https://automationteststore.com/index.php?rt=account/forgotten/loginname">Forgot your login?</a>
								<br>
				<br>
				<button type="submit" class="btn btn-orange pull-right" title="Login">
					<i class="fa fa-lock"></i>
					Login				</button>
			</fieldset>

Login error:
<div class="alert alert-error alert-danger">
<button type="button" class="close" data-dismiss="alert">×</button>
Error: Incorrect login or password provided.</div>

--my account--
URL: https://automationteststore.com/index.php?rt=account/account

<div class="sidewidt">
	<h2 class="heading2"><span>My Account</span></h2>
	<div class="myaccountbox">
		<ul class="side_account_list">
		  <li class="selected">
		  	<a href="https://automationteststore.com/index.php?rt=account/account"><i class="fa fa-user fa-fw"></i>&nbsp; Account Dashboard</a>
		  </li>	

		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/wishlist"><i class="fa fa-star fa-fw"></i>&nbsp; My wish list</a>
		  </li>	

		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/edit"><i class="fa fa-edit fa-fw"></i>&nbsp; Edit account details</a>
		  </li>	
		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/password"><i class="fa fa-key fa-fw"></i>&nbsp; Change password</a>
		  </li>	
		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/address"><i class="fa fa-book fa-fw"></i>&nbsp; Manage Address Book</a>
		  </li>		      


		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/history"><i class="fa fa-briefcase fa-fw"></i>&nbsp; Order history</a>
		  </li>	  		
		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/transactions"><i class="fa fa-money fa-fw"></i>&nbsp; Transaction history</a>
		  </li>	  		

		  		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/download"><i class="fa fa-cloud-download fa-fw"></i>&nbsp; Downloads</a>
		  </li>	  		


		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/notification"><i class="fa fa-bullhorn fa-fw"></i>&nbsp; Notifications</a>
		  </li>	  		



		  <li>
		  	<a href="https://automationteststore.com/index.php?rt=account/logout"><i class="fa fa-lock fa-fw"></i>&nbsp; Logoff</a>
		  </li>	  		

		</ul>
	</div>

	</div>

--Lipstick datasheet--
URL: https://automationteststore.com/index.php?rt=product/product&product_id=59

<fieldset>
																														<div class="form-group">
																								<label class="control-label">Color</label>
																								<div class="input-group col-sm-10">
													<select name="option[305]" id="option305" class="form-control " data-placeholder="" data-attribute-value-id="">
			<option value="615">Viva Glam IV  </option>
			<option value="616">Viva Glam II  </option>
			<option value="617">Viva Glam VI 1.88€ (975 In Stock)</option>
	</select>
												</div>
											</div>


																											<div class="form-group mt20">
										<div class="input-group col-sm-4">
											<span class="input-group-addon">Qty:</span>
											<input type="text" name="quantity" id="product_quantity" value="1" placeholder="" class="form-control short" size="3">
										</div>
																													</div>

									<div class="form-group mt20 mb10 total-price-holder" style="display: block; visibility: visible;">
										<label class="control-label">
											Total Price:&nbsp;&nbsp;
											<span class="total-price">4.69€</span>										</label>
									</div>


									<div>
										<input type="hidden" id="product_product_id" name="product_id" value="59"><input type="hidden" id="product_redirect" name="redirect" value="https://automationteststore.com/index.php?rt=product/product&amp;product_id=59">									</div>

									<div class="mt20 ">
																														<ul class="productpagecart">
											<li>												<a href="#" onclick="$(this).closest('form').submit(); return false;" class="cart">
													<i class="fa fa-cart-plus fa-fw"></i>
													Add to Cart												</a>
																							</li>
										</ul>
																														<a class="productprint btn btn-large" href="javascript:window.print();">
											<i class="fa fa-print fa-fw"></i>
											Print										</a>
																			</div>

																											<div class="wishlist">
										<a class="wishlist_remove btn btn-large" href="#" onclick="wishlist_remove(); return false;" style="display: none;">
											<i class="fa fa-trash-o fa-fw"></i>
											Remove from wish list										</a>
										<a class="wishlist_add btn btn-large" href="#" onclick="wishlist_add(); return false;">
											<i class="fa fa-plus-square fa-fw"></i>
											Add to wish list										</a>
									</div>
																	</fieldset>

--Update and checkout--
URL: https://automationteststore.com/index.php?rt=checkout/cart

<div class="pull-right mb20">
										<a href="#" onclick="save_and_checkout('checkout/shipping'); return false;" id="cart_checkout1" class="btn btn-orange pull-right" title="Checkout">
					<i class="fa fa-shopping-cart fa-fw"></i>
					Checkout				</a>
						<button title="Update" class="btn btn-default pull-right mr10" id="cart_update" value="cart" type="submit">
				<i class="fa fa-refresh"></i>
				Update			</button>
					</div>

--Lip search results--
URL: https://automationteststore.com/index.php?rt=product/search&keyword=lip&category_id=0

<div class="thumbnails grid row list-inline">
			<div class="col-md-3 col-sm-6 col-xs-12">
			<div class="fixed_wrapper">
				<div class="fixed">
					<a class="prdocutname" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=116" title="New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals">New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals</a>
									</div>
			</div>
			<div class="thumbnail">
												<a href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=116"><img src="//automationteststore.com/image/thumbnails/18/78/new_ladies_red3_jpg-100225-250x250.jpg" width="250" height="250" alt=""></a>

				<div class="shortlinks">
					<a class="details" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=116">View</a>
											<a class="compare" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=116#review">Write Review</a>
														</div>
				<div class="blurb"></div>
													<div class="pricetag jumbotron">
													<a data-id="116" href="https://automationteststore.com/index.php?rt=product/product&amp;product_id=116" class="productcart" title="Add to Cart">
								<i class="fa fa-cart-plus fa-fw"></i>
							</a>

						<div class="price">
															<div class="oneprice">24.40€</div>
													</div>
											</div>
							</div>
		</div>
			<div class="col-md-3 col-sm-6 col-xs-12">
			<div class="fixed_wrapper">
				<div class="fixed">
					<a class="prdocutname" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=55" title="LE ROUGE ABSOLU Reshaping &amp; Replenishing LipColour SPF 15">LE ROUGE ABSOLU Reshaping &amp; Replenishing LipColour SPF 15</a>
									</div>
			</div>
			<div class="thumbnail">
									<span class="sale"></span>
												<a href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=55"><img src="//automationteststore.com/image/thumbnails/18/6d/demo_product09_4_jpg-100059-250x250.jpg" width="250" height="250" alt=""></a>

				<div class="shortlinks" style="display: none;">
					<a class="details" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=55">View</a>
											<a class="compare" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=55#review"><img class="rating" src="storefront/view/default/image/stars_4.png" alt="4 out of 5 Stars!" width="64" height="12"></a>
														</div>
				<div class="blurb"></div>
													<div class="pricetag jumbotron">
													<a data-id="55" href="https://automationteststore.com/index.php?rt=product/product&amp;product_id=55" class="productcart" title="Add to Cart">
								<i class="fa fa-cart-plus fa-fw"></i>
							</a>

						<div class="price">
															<div class="pricenew">25.34€</div>
								<div class="priceold">27.22€</div>
													</div>
											</div>
							</div>
		</div>
			<div class="col-md-3 col-sm-6 col-xs-12">
			<div class="fixed_wrapper">
				<div class="fixed">
					<a class="prdocutname" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=59" title="Viva Glam Lipstick">Viva Glam Lipstick</a>
									</div>
			</div>
			<div class="thumbnail">
												<a href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=59"><img src="//automationteststore.com/image/thumbnails/18/70/demo_product08_jpg-100097-250x250.jpg" width="250" height="250" alt=""></a>

				<div class="shortlinks" style="display: none;">
					<a class="details" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=59">View</a>
											<a class="compare" href="https://automationteststore.com/index.php?rt=product/product&amp;keyword=lip&amp;category_id=0&amp;product_id=59#review">Write Review</a>
														</div>
				<div class="blurb"></div>
													<div class="pricetag jumbotron">
													<a data-id="59" href="https://automationteststore.com/index.php?rt=product/product&amp;product_id=59" class="productcart" title="Add to Cart">
								<i class="fa fa-cart-plus fa-fw"></i>
							</a>

						<div class="price">
															<div class="oneprice">4.69€</div>
													</div>
											</div>
							</div>
		</div>
	</div>

--No findings--
URL: https://automationteststore.com/index.php?rt=product/search&keyword=dsadfsadsa&category_id=0

<div class="contentpanel">

	<h4 class="heading4">Search Criteria</h4>
	<div class="form-inline">
		<fieldset>
			<div class="form-group col-xs-6 col-sm-2 col-lg-2">
				<div class="input-group">
				    <input type="text" name="keyword" id="keyword" value="" placeholder="" class="form-control ">
&nbsp;
				</div>
			</div>		
			<div class="form-group col-xs-6 col-sm-2 col-lg-2">
				<div class="input-group">
				    <select name="category_id" id="category_id" class="form-control " data-placeholder="">
			<option value="0" selected="selected">All Categories</option>
			<option value="0,68">&nbsp;&nbsp;&nbsp;Apparel &amp; accessories</option>
			<option value="0,36">&nbsp;&nbsp;&nbsp;Makeup</option>
			<option value="0,43">&nbsp;&nbsp;&nbsp;Skincare</option>
			<option value="0,49">&nbsp;&nbsp;&nbsp;Fragrance</option>
			<option value="0,58">&nbsp;&nbsp;&nbsp;Men</option>
			<option value="0,52">&nbsp;&nbsp;&nbsp;Hair Care</option>
			<option value="0,65">&nbsp;&nbsp;&nbsp;Books</option>
	</select>
&nbsp;
				</div>
			</div>		
			<div class="form-group col-xs-12 col-sm-3 col-lg-3">
				    <label class="checkbox" for="description"><input style="position: relative; margin-left: 0;" type="checkbox" class="" name="description" id="description" value="1">
Search in product descriptions</label>&nbsp;
			</div>		
			<div class="form-group col-xs-12 col-sm-3 col-lg-3">
				    <label class="checkbox" for="model"><input style="position: relative; margin-left: 0;" type="checkbox" class="" name="model" id="model" value="1">
Search in product model</label>&nbsp;
			</div>		
			<div class="form-group col-xs-12 col-sm-2 col-lg-2">
				<div class="input-group">
				    <button type="button" id="search_button" class="btn btn-default" title="Search">
<i class="fa fa-search"></i>
 Search</button>
				</div>
			</div>		
		</fieldset>
	</div>

	<h4 class="heading4">Products meeting the search criteria</h4>
			<div>
			There is no product that matches the search criteria.		</div>


</div>

--Confirm order button--
URL: https://automationteststore.com/index.php?rt=checkout/confirm

<button id="checkout_btn" onclick="confirmSubmit();" class="btn btn-orange pull-right lock-on-click" title="Confirm Order" data-loading-text="<i class='fa fa-refresh fa-spin'></i>">
    	    <i class="fa fa-check"></i>
    	    Confirm Order    	</button>

--order processed--
URL: https://automationteststore.com/index.php?rt=checkout/success

<div class="col-md-12 col-xs-12 mt20">

		<div class="">
		<h1 class="heading1">
  <span class="maintext"><i class="fa fa-thumbs-up"></i> Your Order Has Been Processed!</span>
  <span class="subtext"></span>
</h1>

<div class="contentpanel">

<section class="mb40">
<h4 class="hidden">&nbsp;</h4>
	<p></p><p>Your order #49802 has been created!</p>
			<p>You can view your order details by going to the <a href="https://automationteststore.com/index.php?rt=account/invoice&amp;order_id=49802">invoice page</a>.</p>
			<p>Please direct any questions you have to the <a href="https://automationteststore.com/index.php?rt=content/contact">store owner</a>.</p>
			<p>Thank you for shopping with us!</p><p></p>

	<a href="https://automationteststore.com/" class="btn btn-default mr10" title="Continue">
	    <i class="fa fa-arrow-right"></i>
	    Continue	</a>
</section>

</div>		</div>

				</div>

--Empty cart--
URL: https://automationteststore.com/index.php?rt=checkout/cart

<div class="col-md-12 col-xs-12 mt20">

		<div class="">
		<h1 class="heading1">
  <span class="maintext"><i class="fa fa-frown"></i> Shopping Cart</span>
  <span class="subtext"></span>
</h1>

<div class="contentpanel">

	Your shopping cart is empty!	
	<div class="container-fluid">
	    	<div class="col-md-4 mt20 mb20">

	    		<a href="https://automationteststore.com/" class="btn btn-default mr10" title="Continue">
	    		    <i class="fa fa-arrow-right"></i>
	    		    Continue	    		</a>
	    	</div>	
	</div>

</div>		</div>

				</div>
"""
thread = client.beta.threads.create()

client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"""
    Here is 10 snippets of HTMl code:
{full_html}
    There are 7 flows for 7 tests:
    The first: Click Login or register from login header; fill the username, password input with invalid info and click the login button (title=Login) from login Box; check if the error message pops up from the login box with error
    The second: Click Login or register from login header; fill the username, password input with valid info (valid username: csaba.kelemen, valid password: tesztteszt1) and click the login button (title=Login) on login Box; check if element from my account page can be seen from Update and checkout (dont use the URL for this part).
    The third: Click on the search-bar input, type "Lipstick" and press the enter key from login header; in this case there is no grid you can immediately click add to cart (href) from the Lipstick datasheet; and see if the checkout button can be seen afterwards from Update and checkout (dont use the URL for this part).
    the fourth: Click on the search-bar input, type "Lip" and press the enter key from login header; click the Viva Glam Lipstick titled element by the selector (a[title="Viva Glam Lipstick"]) from the Lib search results;after that click add to cart (href) from lipstick datasheet; and see if the checkout button can be seen afterwards from Update and checkout (dont use the URL for this part).
    the fifth: Click on the search-bar input, type some nonsense and press the enter key from login header; see if the 'There is no product that matches the search criteria.' div is there (dont use the URL for this part).
    the sixth: Click Checkout on top header (first of the a.menu_checkout) from login header; after the Checkout information appears, wait for Confirm order button, then click that button from confirm order html snippet; check url to see if the order was successful (https://automationteststore.com/index.php?rt=checkout/success).
    The seventh: Click Checkout on top header (first of the a.menu_checkout) from login header; and check url to see if cart is empty (https://automationteststore.com/index.php?rt=checkout/cart).
    You have to generate 4 .py code(3 POM code and 1 pytest code).
     I will separate and use your answer with the re.split(r"\n{3,}",message_content.strip()) python function 
     so you must separate the four code that way!
I already used two types of fixture for the pytests: one is named ’set_up_fresh_browser’
 where there is no pre-loaded context for the browser, it is used by the successful and the unsuccessful login tests.
  The second one called ’set_up_logged_in_browser’ which is using my already logged in context state for the product
   and the cart tests. Fixtures format: def funtion(set_up_fresh_browser):
   The POMs and their classes should be called: generated_loginPage file and LoginPage class,
    generated_product file and Product class, generated_cart file and Cart class
   Please take note, that the environment where the test runs is really slow (the elements're loading in slowly).
   The page for the test is https://automationteststore.com/
   Use synchronous playwright and the look out for the matching elements before clicking, never use the asynchronous playwright module.
   Get only one element per every locator.
"""
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=ASSISTANT_ID
)

while True:
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run_status.status == "completed":
        break
    elif run_status.status == "failed":
        raise Exception("Assistant run failed.")
    time.sleep(1)

time.sleep(15)
messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

message_content = messages[0].content[0].text.value
# print(message_content)

code_list = re.split(r"(?:\s*\n\s*){3,}", message_content.strip())

with open("generated_poms_and_test/generated_loginPage.py", "w") as f1, \
        open("generated_poms_and_test/generated_product.py", "w") as f2, \
        open("generated_poms_and_test/generated_cart.py", "w") as f3, \
        open("generated_poms_and_test/generated_test_main.py", "w") as f4:
    f1.write(f"{code_list[0]}")
    f2.write(f"{code_list[1]}")
    f3.write(f"{code_list[2]}")
    f4.write(f"{code_list[3]}")