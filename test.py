from bardapi import Bard

token = 'YAiv-auUY6qYvw1a0GH8HOE19GoNWgpY25TfsUcCqZdktsJ6-ByL6S8XMzmP3xYjV4GFXA.'
bard = Bard(token=token)
response = bard.get_answer("what is machine learning")['content']
print(response)
