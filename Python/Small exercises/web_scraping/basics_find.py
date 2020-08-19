#check robots.txt file
#Beautiful soup allows us to navigate through html with python
#does not download html
#need requests module for that
#html comes back as a large string


#can navigate by tage name, use find or find_all 
#also with css selector


#CSS selectors:

"""select by id of foo: #food
#d = soup.select("#first") 
select by class of bar: .bar
select children: div > p
select descendents: div p


#get_text = access the inner text in an element
#name - tag name of given element
attrs - dictionary of attributes
can also access attribute values using brackets"""


"""navigating via tags:
parent/parents
contents
next_sibling/next_siblings

via searching"
find_parent/find_parents
find_next_sibling/find_next_siblings
find_previous_sibling/find_previous_siblings"""