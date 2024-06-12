class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            print('Author is not of type Author')
            return
        self._author = new_author
            
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            print('Magazine is not of type Magazine')
            return
        self._magazine = new_magazine
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            print('Title must be of type string')
            return
        if not (5 <= len(new_title) <= 50):
            print('Title must be between 5 to 50 characters')
            return
        if hasattr(self, '_title'):
            print('Title has already been set')
            return
        self._title = new_title
        
    def __repr__(self) -> str:
        return f'<Article {self.title} {self.author.name} {self.magazine.name}>'
    
class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            print('Author Name has been already set')
            return
        if not isinstance(new_name, str):
            print('Name should be of type string')
            return
        if not len(new_name) > 0:
            print('Author name should be more than 0 characters')
            return
        self._name = new_name

    def articles(self):
        results = []
        for article in Article.all:
            if article.author is self:
                results.append(article)
        return results

    def magazines(self):
        results = []
        for article in self.articles():
            results.append(article.magazine)
        return list(set(results))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics_list = []
        if not len(self.articles()) > 0:
            print('author has no articles written')
            return None
        for magazine in self.magazines():
            topics_list.append(magazine.category)
        return list(set(topics_list))
    
    def __repr__(self) -> str:
        return f'<Author {self.name}'

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print('name must be of type string')
            return
        if not ( 2 <= len(new_name) <= 16 ):
            print('length must be between 2 to 16 chars')
            return
        self._name = new_name
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            print('category must be of type string')
            return
        if not len(new_category) > 0:
            print('Categories must be longer than 0 characters')
            return
        self._category = new_category

    def articles(self):
        results = []
        for article in Article.all:
            if article.magazine is self:
                results.append(article)
        return results

    def contributors(self):
        results = []
        for article in self.articles():
            results.append(article.author)
        return list(set(results))

    def article_titles(self):
        results = []
        if len(self.articles()) > 0:
            for article in self.articles():
                results.append(article.title)
        else:
            return None
        return results

    def contributing_authors(self):
        authors = []
        contributors = []
        count = {}
        for article in self.articles():
            authors.append(article.author)
        for author in authors:
            count[author] = authors.count(author)
        for key in count:
            if count[key] > 2:
                contributors.append(key)
        if len(contributors) > 0:
            return contributors
        else:
            return None
        
    def __repr__(self) -> str:
        return f'<Magazine {self.name} {self.category}>'
        

if __name__ == '__main__':
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")
    Article(author_1, magazine_1, "How to wear a tutu with style")
    Article(author_1, magazine_1, "How to be single and happy")
    Article(author_1, magazine_1, "Dating life in NYC")
    Article(author_1, magazine_2, "Carrara Marble is so 2020")
    Article(author_2, magazine_2, "2023 Eccentric Design Trends")
    
    print(magazine_1.contributing_authors())
    print(magazine_2.contributing_authors())