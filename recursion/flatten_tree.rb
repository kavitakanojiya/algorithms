# To be implemented #

require 'json'

class FlattenTree
  # File: animalia.json
  # Purpose: Flatten the tree into a hash by maintaing parent-child relationship.
  def initialize
    @data = JSON.parse(File.open("/Users/kavitakanojiya/Desktop/Projects/algorithms/recursion/animalia.json").read)
    @taxonomies = @data['data']['tree']['animalia']

    @current_branch = @taxonomies.clone

    @flattened_structure = Hash.new
  end

  def recurse(object)
    @current_branch.each do |key, value|
      # Step 1: Pick label and path and consider it as a single hash item. Add it to @flattened_structure.
    end
  end

  def process
    recurse(@current_branch)
  end
end

klass = FlattenTree.new
klass.process


# Parse Tree Using Recursion
# ```ruby
# klass = TaxonomyKeywordsProcessor.new
# klass.process

# OUTPUT:

# {
#    "animalia.coelenterata.hydrozoa.hydra":{
#       "path":"animalia.coelenterata.hydrozoa.hydra",
#       "label":"Hydra",
#       "tk_id":"90c9ff90c94ced4b85b9f5ca37779e42"
#    },
#    "animalia.coelenterata.hydrozoa.physalia":{
#       "path":"animalia.coelenterata.hydrozoa.physalia",
#       "label":"Physalia",
#       "tk_id":"90c9ff90c94ced4b85b9f5ca37779e42"
#    },
#    "animalia.coelenterata.scyphozoa.aurelia":{
#       "path":"animalia.coelenterata.scyphozoa.aurelia",
#       "label":"Aurelia",
#       "tk_id":"9e4187ac92d86dd04ce80678d3a73c40"
#    }
# }
# ```
