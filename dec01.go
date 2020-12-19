package main
import (
    "bufio"
    "fmt"
    "log"
	"os"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func inSliceN(n int, s []int) bool {
	for _,a := range s {
		if n == a {
			return true
		}
	}
	return false
}

func main() {
    file, err := os.Open("input/dec01")
	if err != nil {
		log.Fatal(err)
	}
    defer file.Close()

	var nums []int
	scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		num,_ := strconv.Atoi(scanner.Text())
		nums = append(nums, num)
	}
	
	if err := scanner.Err(); err != nil {
        log.Fatal(err)
	}

	var part1,part2 int
	for i,_ := range nums {
		b := 2020 - nums[i]
		if inSliceN(b, nums) {
			part1 = b * nums[i]
		}
		for j,_ := range nums {
			c := 2020 - (nums[i] + nums[j])
			if inSliceN(c, nums) {
				part2 = c * nums[i] * nums[j]
			}
		}
	}
	fmt.Println(part1)
	fmt.Println(part2)
}