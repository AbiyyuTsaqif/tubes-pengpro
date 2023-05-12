package main
import "fmt"

func main() {
    var r,t int
    var c float64
    fmt.Scan(&r, &t)
    c = (1/3)* 3.14* (r*r)* t
    fmt.Println("%.2f", c)
}