# robonomics_contracts

### remote
https://github.com/airalab/robonomics_contracts

## Commit #1 

### Hash
[b0c6d713f5355a850cdc7c0cb4b00f5fb088c587](https://github.com/airalab/robonomics_contracts/commit/b0c6d713f5355a850cdc7c0cb4b00f5fb088c587)

### Message
Fix keepalive deadlock when sender is not in memebers

### Antipattern Category
X

### Keyword
deadlock

### Note
This commit fixes an infinite loop in a low-level code. It is a simple bug fix. There is no antipattern. This commit make sure that the member (a key in the array) exists before entering an infinite loop for finding the member.

## Commit #2

### Hash
[ca2262837e070a3ea011b1faef014f44d2c0d6b7](https://github.com/airalab/robonomics_contracts/commit/ca2262837e070a3ea011b1faef014f44d2c0d6b7)

### Message
Fixed deadlock when marker point out of members

### Antipattern Category
X

### Keyword
deadlock

### Note
This commit fixes an infinite loop in a low-level code. It is a simple bug fix. There is no antipattern. This commit changes a `while ... do` to `do ... while` to make sure that it does not lead to the infinite loop because of the marker pointing out of the array.