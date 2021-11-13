import hashlib

class Block:
   def __init__(self, nr, data, p_hash):
      self.nr = nr
      self.data = data
      self.p_hash = p_hash
      self.hash = hashlib.sha256((str(nr) + data + p_hash).encode()).hexdigest()
        
   def __str__(self):
      return '{}:::{};{}'.format(self.nr, self.hash, self.data)
        
class BlockChain():
   def __init__(self):
      genesis_block = Block(0, 'GENESIS', '0'*64)
      self.blocks = [genesis_block]
        
   def append(self, data):
      self.blocks.append(
         Block(
            len(self.blocks),
            data,
            self.blocks[len(self.blocks)-1].hash
        )
      )
        
   def __str__(self):
      res = ''
      for block in self.blocks:
         res += '{}\n'.format(block)
      return res
        
   def validate(self):
      for i in range(1, len(self.blocks)):
         if self.blocks[i].nr != i:
            print('Manipulation der TAC in Block {} entdeckt!'.format(i))
            return False
         if self.blocks[i-1].hash != self.blocks[i].p_hash:
            print('Manipulation der Daten in Block {} entdeckt!'.format(i-1))
            return False
      print('Blockchain valide!')
      return True
        
bc = BlockChain()
bc.append('<Asuna> sendet <Kazuto> <0.002 BTC>')
bc.append('<Hitagi> sendet <Mayuri> <0.087 BTC>')
bc.append('<Mamoru> sendet <Usagi> <1.2 BTC>')
bc.append('<Usagi> sendet <Asuna> <0.6 BTC>')

bc.blocks[3] = Block(3, '<Mamoru> sendet <Usagi> <1.5 BTC>', bc.blocks[2].p_hash)

print(bc)
bc.validate()
