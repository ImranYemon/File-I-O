📂 Understanding File I/O in Python
File I/O in Python refers to how a program interacts with files — to read data from or write data to files stored on your computer.

🔹 Why File I/O?
File I/O is useful when you need to:

Save program output to a file (like logs or reports)

Read data from a file (like user input or configuration)

Store data between runs of your program

🔸 Opening Files
Before you can read or write to a file, you must open it. When opening a file, you specify a mode that tells Python what you want to do:

"r" = Read (default)

"w" = Write (overwrites file if it exists)

"a" = Append (adds content to the end)

"x" = Create (fails if file already exists)

"b" = Binary mode (for images, PDFs, etc.)

📖 Reading Files
Reading a file means loading its content into your program so you can use it. Python lets you read the whole file at once or line by line.

✍️ Writing and Appending
You can write new content to a file or add new lines to the end of an existing file. Be careful: write mode can delete existing data.

✅ Using with
The with statement is the safest way to work with files. It automatically closes the file after you're done, even if an error happens.

🔐 Always Close Files
If you open a file manually (without with), always remember to close it after finishing. This frees up system resources and avoids errors.
