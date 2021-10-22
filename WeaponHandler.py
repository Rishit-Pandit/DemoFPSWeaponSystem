# Placeholder spawn function (this function is generaly provided by the engine)
def spawn(obj, transform, acc):
  print(f"Spawning {obj.name}")
	pass

# Placeholder function for playing animations (this function is generaly provided by the engine)
def play(anim):
	print(f"Playing {anim}")
  pass


# Here we define the Projectile Class to be used as ammo by the weapon
class FastProjectile():
	def __init__(self, name, mesh, acc):
		self.name = name                                      # The name of the ammo
		self.mesh = mesh                                      # The placeholder for the mesh used
		self.acc = acc                                        # The acceleration of the bullet (to supply to the spawn function)


# Here we define the main Weapon class
class FastProjectileWeapon():
	def __init__(self, name, mesh, projectile, magazineSize, magazineNo, fireAnim, muzzleLocation, projectileAcc, reloadAnim, mode, changeModeAnim):
		self.name = name                                      # The name of the weapon
		self.mesh = mesh                                      # The placeholder for the mesh used
		self.ammo = projectile                                # The ammo used (the class instance)
		self.magSize = magazineSize                           # The size of the magazine of the weapon
		self.magNo = magazineNo                               # The number of magazines of the weapon
		self.currentMag = self.magSize                        # Current number of bullets in Magazine
		self.currentMagNo = self.magNo                        # Current number of Magazines
		self.spareAmmo = 0                                    # The Spare ammo (separate from the currentMag and currentMagNo)
		self.mode = mode                                      # The list of Firing Modes
		self.currentModei = 0                                 # The index of the current firing mode
		self.currentMode = self.mode[self.currentModei]       # The current firing mode
		self.fireAnim = fireAnim                              # The placeholder for the Fire Animation
		self.reloadAnim = reloadAnim                          # The placeholder for the Reload Animation
		self.changeModeAnim = changeModeAnim                  # The placeholder for the Change Fire Mode Animation
		self.transform = [0, 0, 0]                            # The placeholder world transform of the Weapon (this value is received from the engine not predefined)
		self.muzzleLoc = muzzleLocation                       # The muzzle location where the bullet is spawned

  # The Fire function
	def fire(self):
		if self.currentMag > 0:                               # Check if there are bullets in the current magazine
			spawn(self.ammo, (self.transform + self.muzzleLoc), self.ammo.acc)
			play(self.fireAnim)
			self.currentMag -= 1                                # Decrement the number of bullets in the current magazine
			print(f"Current Mag: {self.currentMag}, Current Mag No: {self.currentMagNo}, Spare Ammo: {self.spareAmmo}")
		elif self.currentMag == 0 and (self.currentMagNo != 0 or self.spareAmmo > 0):
                                                          # Check if there are no bullets in the current mag and (number of mags is not equal to 0 or there is some spare ammo)
			self.reload()                                       # If yes then reload and increase the number of bullets in the current mag.
		else :
			pass
  
  # The Reload function
	def reload(self):
		if self.currentMag == self.magSize or (self.currentMagNo == 0 and self.spareAmmo == 0):
			pass
		elif self.currentMag == 0:
			play(self.reloadAnim)
			if self.currentMagNo == 0 and self.spareAmmo > 0:
				self.currentMag = self.spareAmmo
				self.spareAmmo = 0
			else :
				self.currentMagNo -= 1
				self.currentMag = self.magSize
		else:
			play(self.reloadAnim)
			if self.currentMagNo != 0 and self.spareAmmo == 0:
				self.spareAmmo = self.currentMag
				self.currentMag = self.magSize
				self.currentMagNo -= 1
			elif self.currentMagNo != 0 and self.spareAmmo > 0:
				self.spareAmmo = self.spareAmmo + self.currentMag
				self.currentMagNo -= 1
				self.currentMag = self.magSize
				if self.spareAmmo >= self.magSize:
					self.spareAmmo -= self.magSize
					self.currentMagNo += 1
		print(f"Current Mag: {self.currentMag}, Current Mag No: {self.currentMagNo}, Spare Ammo: {self.spareAmmo}")
  
  # The Change Firiong Mode function
	def changeMode(self):
		self.currentModei = self.mode.index(self.currentMode)
		if len(self.mode) > 1:
			play(self.changeModeAnim)
			if self.currentModei < len(self.mode) - 1:
				self.currentModei += 1
				self.currentMode = self.mode[self.currentModei]
			else :
				self.currentModei -= 1
				self.currentMode = self.mode[self.currentModei]
		else:
			pass
