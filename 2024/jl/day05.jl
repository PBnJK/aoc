# Day 5: Print Queue

include("util.jl")

using .Util
using DataStructures: DefaultDict

r, p = split.(strip.(split(Util.getinputn("day05.txt"), "\n\n")), "\n")
rules = DefaultDict(Set)
for rule ∈ r
	f, t = split(rule, "|")
	push!(rules[f], t)
end

function validate()
	valid, invalid = [], []

	for pages ∈ p
		visited = Set()
        good = true

		pages = split(pages, ",")
        for page ∈ pages
			if !isdisjoint(rules[page], visited)
                good = false
                break
			end

            push!(visited, page)
		end

		if good push!(valid, pages) else push!(invalid, pages) end
	end

	return valid, invalid
end

function star1()
	valid, _ = validate()

	total = sum(parse(Int64, x[length(x) ÷ 2 + 1]) for x ∈ valid)
	println("- $total")
end

function star2()
	_, invalid = validate()

	compare(a, b) = a ∈ rules[b]
	sort!.(invalid, lt=compare)

	total = sum(parse(Int64, x[length(x) ÷ 2 + 1]) for x ∈ invalid)
	println("- $total")
end

star1()
star2()

