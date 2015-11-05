# NYPL Conclusion Report

**Author**: Yingyu Wu

**Email** : ywu23@kent.edu

## 1 Testing Strategy

### 1.1 Overall strategy

10 test cases are defined and test cases are tested in both http://catalog.nypl.org/ and http://browse.nypl.org

### 1.2 Test Selection

A black-box technique is employed for the system tests 

  

## 2 Test Cases

| # | Test Name | Expected Value | Actual Result In http://catalog.nypl.org/| Actual Result In http://browse.nypl.org |
|:-:|:----------|:----------------|:--------------|:---------:|
| 1 | Search same keyword in two websites | return same amount of results| return same amount of results | return same amount of results |
| 2 | Search keywords in two websites | return expect results| return expect results | return expect results |
| 3 | Test if both websites can handle invalid keyword | Both can handle | invalid keyword return 'no result found' | invalid keyword return 'no result found' |
| 4 | Test ISBN/ISSN search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword can return the expect result | invalid keyword are handled |
| 5 | Test Call Number search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled |
| 6 | Test Author search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled, certain Author is not found |
| 7 | Test Title search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled |
| 8 | Test Subject search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled, amount of result are not same as the amount in http://catalog.nypl.org/|
| 9 | Test Genre search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled, amount of result are not same as the amount in http://catalog.nypl.org/|
| 10| Test Journal Title search with valid and invalid keywords | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled | Valid keyword and invalid keyword are handled, amount of result are not same as the amount in http://catalog.nypl.org/ |

## 3 Obversation
Seems the algorithm of searching books or journals are different in the two websites. Some authors can be found in the new site but not in the old site. <br>
In the new site, there's no option for searching by ISN or Call Number although user can enter the those in the search box directly. <br>
The results of searching certain keywords are not returning the same amount of results.<br>
In my opinion, the old site did better on filering the results based on different categories. The new site always return more results than I need. The style of the new site looks much better then the old one, especially for showing the result items.
 

## 4 Testing Result
![Alt text](result1.PNG)
<br>
![Alt text](result2.PNG)












