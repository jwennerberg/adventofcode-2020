package main
import (
    "bufio"
    "fmt"
    "log"
	"os"
	"strconv"
	s "strings"
)

func inSliceN(n int, s []int) bool {
	for _,a := range s {
		if n == a {
			return true
		}
	}
	return false
}

func getRange(r string) (int, int) {
	s := s.Split(r, "-")
	start,_ := strconv.Atoi(s[0])
	end,_ := strconv.Atoi(s[1])
	return start, end
}

func main() {
    file, err := os.Open("input/dec02")
	if err != nil {
		log.Fatal(err)
	}
    defer file.Close()

	var part1_match int
	var part2_match int
	scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		i := s.Split(scanner.Text(), " ")
		pass := i[2]
		start,end := getRange(i[0])
		char := i[1][:1]
		if s.Count(pass, char) >= start && s.Count(pass, char) <= end {
			part1_match++
		}
		c_pos1 := pass[(start - 1):start]
		c_pos2 := pass[(end -1):end]
		if c_pos1 == char && c_pos2 != char {
			part2_match++
		}
		if c_pos2 == char && c_pos1 != char {
			part2_match++
		}
	}
	if err := scanner.Err(); err != nil {
        log.Fatal(err)
	}

	fmt.Println(part1_match)
	fmt.Println(part2_match)
}