critics = {
	'Lisa Rose': {'Lady in the Water':2.5,
					'Snakes on a Plane':3.5,
					'Just My Luck':3.0,
					'Superman Returns':3.5,
					'You, Me and Dupree':2.5,
					'The Night Listener':3.0
	},
	'Gene Seymour':{'Lady in the Water':3.0,
					'Snakes on a Plane':3.5,
					'Just My Luck':1.5,
					'Superman Returns':5.0,
					'You, Me and Dupree':3.5,
					'The Night Listener':3.0
	},
	'Michael Phillips':{'Lady in the Water':2.5,
					'Snakes on a Plane':3.0,
					'Superman Returns':5.0,
					'The Night Listener':4.0
	},
	'Claudia Puig':{'Snakes on a Plane':3.5,
					'Just My Luck':3.0,
					'Superman Returns':4.0,
					'You, Me and Dupree':2.5,
					'The Night Listener':4.5
	},
	'Mick LaSalle':{'Lady in the Water':3.0,
					'Snakes on a Plane':4.0,
					'Just My Luck':2.0,
					'Superman Returns':3.0,
					'You, Me and Dupree':2.0,
					'The Night Listener':3.0
	},
	'Jack Matthews':{'Lady in the Water':3.0,
					'Snakes on a Plane':4.0,
					'Superman Returns':5.0,
					'You, Me and Dupree':3.5,
					'The Night Listener':3.0
	},
	'Toby':{'Snakes on a Plane':4.5,
					'Superman Returns':4.0,
					'You, Me and Dupree':1.0,
	}
}



from math import sqrt
# Returns a distance-based similarity score for person1 and person2

def sim_distance(prefs, person1, person2):
	#distance = 0
	# for item in prefs[person1].keys():
	# 	if item in prefs[person2].keys():
	# 		absolute_distance = float(prefs[person1][item])- float(prefs[person2][item])
	# 		distance += pow(absolute_distance,2)
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	if (len(si) == 0): return 0 
	distance = sum([(prefs[person1][item]-prefs[person2][item])**2 for item in prefs[person1] if item in prefs[person2]])	
	return 1/(1+sqrt(distance))

#print sim_distance(critics, 'Lisa Rose','Gene Seymour')

def sim_pearson(prefs, person1, person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	n = len(si)
	if (n == 0): return 0 
	sum1 = sum(prefs[person1][item] for item in si)
	sum2 = sum(prefs[person2][item] for item in si)

	sum1Sq = sum(pow(prefs[person1][item],2) for item in si)
	sum2Sq = sum(pow(prefs[person2][item],2) for item in si)

	pSum = sum(prefs[person1][item] * prefs[person2][item] for item in si)

	num = pSum - (sum1*sum2)/n
	den = sqrt((sum1Sq - pow(sum1, 2)/n)*(sum2Sq - pow(sum2,2)/n))
	if den == 0: return 0

	r = num/den

	return r


def topMatch(prefs, person,n=6, similarity = sim_pearson):
	# score = {}
	# for other in prefs:
	# 	if other == person: 
	# 		continue
	# 	score[other] = similarity(critics, person, other)
	# score = sorted(score.items(), key=lambda x:x[1], reverse=True)
	# return score[:n]
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

	scores.sort()
	scores.reverse()

	return scores[0:6]

#print topMatch(critics,'Toby',3, sim_pearson)

def getRecommendations(prefs, person, similarity = sim_pearson):
	# score_items = {} 
	# score = {}
	# for other in prefs:
	#  	if other == person: 
	#  		continue
	#  	score[other] = similarity(critics, person, other)

	# for p in prefs:
	# 	if (p != person):
	# 		for item in prefs[p]:
	# 			if (item not in prefs[person]):
	# 				score_items.setdefault(item, None)

	# for item in score_items:
	# 	sum_sim_person = 0
	# 	sum_scores = 0
	# 	for p in prefs:
	# 		if (item in prefs[p]):
	# 			sum_sim_person += score[p]
	# 			sum_scores += score[p] * prefs[p][item]
	# 	score_items[item] = sum_scores/sum_sim_person

	# return sorted(score_items.items(), key = lambda x: x[1], reverse=True)

	total = {}
	sum_sim = {}
	for other in prefs:
		if (other != person):
			sim = similarity(prefs,person, other)
			if sim <= 0: continue
			for item in prefs[other]:
				if (item not in prefs[person]):
					total.setdefault(item, 0)
					total[item] += prefs[other][item] * sim
					sum_sim.setdefault(item, 0)
					sum_sim[item] += sim

	rank = [(total[item]/sum_sim[item], item) for item in total]
	rank.sort()
	rank.reverse()
	return rank




def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item] 
	return result

movies = transformPrefs(critics)
#print topMatch(movies, 'Just My Luck')

print getRecommendations(critics, 'Toby', similarity = sim_distance)

