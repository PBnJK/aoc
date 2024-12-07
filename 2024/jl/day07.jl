# Day 7: Bridge Repair

include("util.jl")

using .Util

data = []
for i ∈ Util.getinput("day07.txt")
	s = split(i, ": ")
	push!(data, (parse(Int64, s[1]), parse.(Int64, split(s[2]))))
end

function star1()
	total = 0
	println("- $total")
end

function star2()
	total = 0
	println("- $total")
end

star1()
star2()

