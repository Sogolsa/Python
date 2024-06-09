# File Handling in Python

## Use files to store and retrieve data in Python

### Working With Text Files:

- Reading from files
- Creating and writing to files

### Open() Method

`<name of file object> = open('<path to file>', '<mode of access>'`

#### Mode of Access

- > 'r' (read)
- > 'w' (write)
- > 'a' (append; add to the end of an existing file)
- > 'r+' (update; for both reading and writing)
- > 't' (text; reads or writes text data; enabled by default)
- > 'b' - (binary; reads in or writes out binary data)

### Working with Pickles:

They convert complex data into a packaged stream of bytes, known as a “pickle,” then write this into a binary file.

- Writing binary files with pickle.dump() `pickle.dump(<object name>, <file object name>)`
- reading binary files with pickle.load() `<object to store into> = pickle.load(<file object>)`

### Handling Specific Errors with try-expect:

- TypeError
- IndexError
- NameError
- ValueError

### Finally block:

finally block will still run even after a return statement, to complete the function.

### Else block:

else block only runs if the try block doesn't encounter any errors.
