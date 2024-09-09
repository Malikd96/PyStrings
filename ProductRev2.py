#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]




reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(reviews, positive_words, negative_words):
    
    p_count = 0
    n_count = 0
    for keyword in positive_words:
        for review in reviews:

            p_count += review.lower().count(keyword)    
    for keyword in negative_words:
        for review in reviews:
            n_count += review.lower().count(keyword)
    return p_count, n_count
       
   
p_count , n_count = tally(reviews, positive_words, negative_words)
print(f"Review: {reviews}")
print(f"Positive Words: {p_count}")
print(f"Negative Words: {n_count}")