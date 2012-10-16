import datetimeclass BrowsedItems(object):	def __init__(self):			self.items = []		pass			def add(self, mediaInfo, providerURLs, path):			self.items.append([mediaInfo, providerURLs, path])				while (len(self.items) > 50):			self.items.pop(0)			def get(self, url):			# Look through each of our items and see if any of them has a URL		# which matches the passed in URL.		result = [elem for elem in self.items if url in elem[1]]		if (len(result) > 0):			return [result[0][0], result[0][2]]		else:			return None	def __str__(self):			return str(self.items)	class RecentItem():	def __init__(		self, mediaInfo, providerURLs	):		self.mediaInfo = mediaInfo		self.providerURLs = providerURLs		self.dateAdded = datetime.now()		class ViewedItems(object):	def __init__(self):			self.items = []			def add(self, mediainfo, path, keep):		# The last element of the path will contain the URL actually played.		played_url = path[-1]['url']				#Log('Trying to add item :' + played_url + ' to recently played list.')				result = [elem for elem in self.items if played_url == elem[2]]				if (len(result) <= 0):			self.items.insert(0,[mediainfo, path, played_url])		else:			# FIXME: Update last accessed time.			pass				#while (len(self.items) > keep):		#	self.items.pop()			def get(self, tv_mode, show):			ret_items = []				for item in self.items:					if (item[0].type == 'movie'):				ret_items.append(item)							else:							# Work out whether the item should be added to the list.				if (tv_mode == 'Episode'):					ret_items.append(item)				elif (tv_mode == 'Season'):									# See if we already have an entry for this show and season.					#					# First, do we have a show name and season to do comparison?					if (item[0].show_name is None or item[0].season is None):											# Don't have, can't compare, so add it in.						ret_items.append(item)											else:											result = [elem for elem in ret_items if (elem[0].show_name == item[0].show_name and elem[0].season == item[0].season)]												# If we don't have an existing item, add ourselves in. Otherwise, ignore it.						if (len(result) <= 0):							ret_items.append(item)									elif (tv_mode == 'Show'):								# See if we already have an entry for this show.					#					# First, do we have a show name to do comparison?					if (item[0].show_name is None or item[0].season is None):											# Don't have, can't compare, so add it in.						ret_items.append(item)											else:											result = [elem for elem in ret_items if (elem[0].show_name == item[0].show_name)]												# If we don't have an existing item, add ourselves in. Otherwise, ignore it.						if (len(result) <= 0):							ret_items.append(item)										# Do we have enough entries?			if (len(ret_items) >= show):				break					return ret_items