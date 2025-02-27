# URL-Shorter-in-Python
This application sets up a rudimentary URL shortening service using Flask. The application makes it easy for users to submit long URLs, and then provides a concise URL in return, which can be used for redirection purposes.

The code defines two main endpoints:

/shorten (POST) - Receives a long URL and returns a short URL. 

/<short_code> (GET) - Receives a short code and redirects the user to the corresponding long URL. 

The data is stored in a Python dictionary (url_mapping), which associates each shortcode with the corresponding long URL.

Steps to get the app working properly:
1. Run the Python code; ![URL_Shorter1](https://github.com/user-attachments/assets/3b09067d-ac1a-4376-8df5-82070bb71863)
2. Open a PowerShell terminal and type the command: curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url":"https://dexonline.ro/"}' ( instead of the website "https://dexonline.ro/" , you can use any other website you want); ![URL_Shorter2](https://github.com/user-attachments/assets/773e926f-39a0-4641-a64d-f7bc54b26627)
3. Open the shortened site returned by PowerShell and you will see that it is the previously entered site (example: https://dexonline.ro/).

Possible improvements:

● Data persistence - Currently, the url_mapping dictionary is lost on every restart. A solution would be to use a database (SQLite, PostgreSQL, etc.).

● URL checking - URL validation would be useful to avoid entering invalid data.

● Graphical user interface - A simple HTML page could be added where users could enter URLs.

#Enjoy
