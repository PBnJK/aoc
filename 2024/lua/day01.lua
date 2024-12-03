-- Day 1: Historian Hysteria

require("util")

local data = InputLines("day01.txt")

local function sep()
	local id1 = {}
	local id2 = {}

	for _, v in pairs(data) do
		if v == "" then
			break
		end

		local _, _, a, b = string.find(v, "(%d+)   (%d+)")
		id1[#id1 + 1] = tonumber(a)
		id2[#id2 + 1] = tonumber(b)
	end

	return id1, id2
end

local function star1()
	local id1, id2 = sep()
	table.sort(id1)
	table.sort(id2)

	local sum = 0
	for i = 1, #id1 do
		sum = sum + math.abs(id1[i] - id2[i])
	end

	print("- " .. sum)
end

local function star2()
	local llist = {}
	local map = {}

	for _, v in pairs(data) do
		if v == "" then
			break
		end

		local _, _, a, b = string.find(v, "(%d+)   (%d+)")
		a = tonumber(a)
		b = tonumber(b)

		llist[#llist + 1] = a
		if map[b] == nil then
			map[b] = 1
		else
			map[b] = map[b] + 1
		end
	end

	local sum = 0
	for _, n in ipairs(llist) do
		sum = sum + (n * (map[n] or 0))
	end

	print("- " .. sum)
end

star1()
star2()
