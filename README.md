# Recommendation-systems
sied project when reading book <Collabrorative Filting>

In this project, we build a recommendation system for different users. We use user-based collabrative filtering to rank the related goods for selected custermer.

1. First we calculate the similarities of all the other users.
2. Then we obtain the weighted sum of the ratings of related goods over all people using weighted_sum = \sum rating_of_goodd * simlarity_of_that person
3. Finally we get the scores for each good and recommend them by reverse order using score = weighted_sum/\sum_of_similarities


Further, we can also use item based filtering (switching item with person) to do recommendations - faster in digital marketing and used by Amazon
