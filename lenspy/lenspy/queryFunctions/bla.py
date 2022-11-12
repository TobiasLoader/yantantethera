def createProfileQuery(handle: str, profilePictureUri = None, followNFTURI = None, FollowModule = None)


	createProfile = """"
		query CreateProfile {
		createProfile(request:{ 
						handle: "{handle}",
						profilePictureUri: {profilePictureUri},
						followNFTURI: {followNFTURI},
						followModule: {followModule}
						}) {
			... on RelayerResult {
			txHash
			}
			... on RelayError {
			reason
			}
			__typename
		}
		}
	""".format(handle=handle,)