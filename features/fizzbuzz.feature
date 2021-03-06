Feature: Simple FizzBuzz
	Implement a simple version of the FizzBuzz game

	Scenario: FizzBuzz
		Given the number <input>
		When I call FizzBuzz
		Then I see the output <output>

	Examples:
		| input | output   |
	    | 0    |  0       |
	    | 1     | 1        |
	    | 2     | 2        |
	    | 3     | Fizz     |
	    | 4     | 4        |
	    | 5     | Buzz     |
	    | 6     | Fizz     |
	    | 10    | Buzz     |
	    | 15    | FizzBuzz |