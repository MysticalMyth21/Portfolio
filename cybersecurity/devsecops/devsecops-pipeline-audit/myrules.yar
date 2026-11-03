rule FindSecrets {
	strings:
		$aws_access = /AKIA[0-9A-Z]{16}/
		$aws_secret = "AWS_SECRET_ACCESS_KEY"
		$password = "password"
		$token = /eyJ[A-Za-z0-9-_]{10,}\.[A-Za-z0-_]{10,}\.[A-Za-z0-9-_]{10,}/
		$privatekey = "BEGIN PRIVATE KEY"
	condition:
		any of them
}
