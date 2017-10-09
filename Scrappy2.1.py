import bs4
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/se/Product/ProductList.aspx?Submit=ENE&N=100829626&IsNodeId=1&bop=And&PageSize=96&order=BESTMATCH'
#my_url_2 = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-2?Tid=7709&PageSize=96&order=BESTMATCH' ?????

print """fetching page this might take a while..."""

client = uReq(my_url)
#client = uReq(my_url_2) ???
page_html = client.read()


client.close()

print "...done"

page_soup = soup(page_html, "html.parser")

#defines where to look for info needed
containers = page_soup.findAll('div',{'class':'item-container'})

for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	price_container = container.findAll("li", {"class":"price-current"})
	price = price_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	#print("shipping:{!s}".format(shipping if shipping: else "free") ????
	print("shipping: " + shipping)
	print("price: " + price)

	









	
		
