# Keep Rolling
Keep Rolling is a parser&interpreter for dice rolls encountered in roleplaying games.

## Language Definition
  * commands consist of exactly **ONE** statement
  * whitespaces and newlines are ignored
  * a statement evaluates to either a number or a list of numbers
  
### Types
#### number
direct creation  
`423 -> 423`  

#### list
direct creation  
`[42, 1337, 11] -> [42, 1337, 11]`  
creation via dice rolling  
`3W6 -> [x, y, z]`  
`4w6 -> [w, x, y, z]`  
`3D6 -> [x, y, z]`  
`4d6 -> [w, x, y, z]`  

### Operations
#### Reduction
general syntax  
`list ! op -> number`  
Supported reduction operations are `+, *, <, >`  
sum: `[1,2,3]!+ -> 6`  
prod: `[2,2,3]!* -> 12`  
greatest: `[1,2,3]!> -> 3`  
least: `[1,2,3]!< -> 1`  

#### Map
general syntax  
`list op number -> list`  
Supported map operations are `+, -, *, /, <, >, =`  
`[2,3,4]+2 -> [4,6,8]`  
`[2,3,4]-2 -> [0,1,2]`  
`[2,3,4]*2 -> [4,6,8]`  
`[2,3,4]/2 -> [1,1,2]`  
`[2,3,4]>2 -> [0,1,1]`  
`[2,3,4]=2 -> [1,0,0]`  
`[2,3,4]<3 -> [1,0,0]`  
