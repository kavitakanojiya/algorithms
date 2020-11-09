require 'json'
require 'active_support'
require 'byebug'

# OBJECTIVE: Iterate over the tree structure and save the immediate parent-child relationship into the database.

# HOW:
#   A tree has a single root node. Here, it is a HASH.
#   Every child nodes will have parent (`tk_id`) generated from their parents.
#   So, if a parent node has 3 child nodes, then parent node ID will be common for all the 3 child nodes.

# EXP:  animalia.json follows tree structure typically.
#       We retain Name, Label till we end up at the leaf node.
#       Saving references for child nodes with respective parent node.
#       Using `ancestry` gem for simplicity to create parent-children association.
# Refer `animalia.json` file for detailed tree structure.

# LIMITATIONS:
#   [TBD] This algorithm does not return the whole hash but it takes immediate action saving to the database as it is iterating over.

class TreeToDatabase
  attr_accessor :items, :taxonomies, :taxon

  def initialize
    self.items      = JSON.parse(File.open('/Users/kavitakanojiya/Desktop/Projects/algorithms/recursion/animalia.json').read)
    self.taxonomies = self.items['data']['tree']['animalia']
    self.taxon      = self.items['data']['name']

    # Cache taxonomies initially for traverse to the bottom of the tree.
    # To retain parent's reference across its children.
    @state          = self.taxonomies.clone

    # Keep track of taxonomy_keywords being updated.
    # `taxonomy_keywords` that remains untouched must be marked as deleted.
    # This will help to track what all keywords were removed from animalia
    @existing_taxons = []
  end

  def process
    recurse(@state)
  end

  # This is iterated at each level.
  # Each level is further a new taxonomy. Hence, creating TaxonomyKeyword for each nodes at each level.
  # Child nodes retain parent reference to create branch between parent-children nodes.
  # Whenever a whole level is iterated, their children are used to create a new tree structure altogether.
  #   ignoring original `@taxonomies` tree structure.

  # Argument `object` is a list of nodes at each level.
  def recurse(object)
    # Step 1: Let the tree only has children nodes and not label & path.
    # `@root` has the group name, hence deleting its references like `label` and `path`
    label    = object.delete('label')
    path     = object.delete('path')

    # Step 2: Initialize to an empty hash to create a new tree picking immediate children from each level considered.
    children = {}

    # Step 3: Iterating over each node considering active level and add it to the database.
    object.each do |key, value|
      # 3.a. Let the current hash only has children nodes, ignore `label`, `path`, & `tk_id`.
      iteratable_hash = value.except('label', 'path', 'tk_id')

      # 3.b. Generate a random hex value and assume it as a parent node ID
      parent_id = SecureRandom.hex

      # 3.c. Assign parent node ID to the child nodes.
      # Desc:
      #   Creating a whole tree from children, each children node must their parent node's reference.
      #   `tk_id` is a reference to parent node and is TaxonomyKeyword#id
      iteratable_hash.values.each do |i_h|
        i_h.merge!('tk_id' => parent_id)
      end

      # 3.d. Save the current node to the database
      # ...

      # 3.e. Retain the topics but from different domains with the same name.
      # Desc:
      #   Possibility that same topic may occur under different domains with same name.
      #   Hence, drilling down the taxonomies using `path` since `path` shall remains unique.
      iteratable_hash.each do |i_key, i_value|
        children[i_value['path']] = i_value
      end

      # 3.f: Do not consider leaf nodes i.e. those have no children to process.

      # 3.g: Capture the parent id generated.
      # Scope: Does nothing.
      @existing_taxons << parent_id
    end

    return if children.empty?

    # Step 3: Re-initialize whole `@state` with a new tree structure (only children from current_level)
    @state = children.clone

    # Step 4: Perform repeatedly till we have an empty tree. Empty tree means no more leaf nodes.
    recurse(@state)
  end
end

klass = TreeToDatabase.new
klass.process

# Output of one of the trees
#
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
#    },
#    "animalia.coelenterata.anthozoa.meandrina":{
#       "path":"animalia.coelenterata.anthozoa.meandrina",
#       "label":"Meandrina",
#       "tk_id":"3aa9888c1bb427da16e2ff3f3dbb75ef"
#    },
#    "animalia.coelenterata.anthozoa.adamsia":{
#       "path":"animalia.coelenterata.anthozoa.adamsia",
#       "label":"Adamsia",
#       "tk_id":"3aa9888c1bb427da16e2ff3f3dbb75ef"
#    },
#    "animalia.platyhelminthes.planeria":{
#       "path":"animalia.platyhelminthes.planeria",
#       "label":"Planeria",
#       "tk_id":"6080f0253967732eb401597fd42b4fff"
#    },
#    "animalia.platyhelminthes.tricladida":{
#       "path":"animalia.platyhelminthes.tricladida",
#       "label":"Tricladida",
#       "tk_id":"6080f0253967732eb401597fd42b4fff"
#    },
#    "animalia.platyhelminthes.trematoda.digenea":{
#       "path":"animalia.platyhelminthes.trematoda.digenea",
#       "label":"Digenea",
#       "tk_id":"6a16bdaea300029da9e85cf6c5122589"
#    },
#    "animalia.platyhelminthes.trematoda.paragonimus":{
#       "path":"animalia.platyhelminthes.trematoda.paragonimus",
#       "label":"Paragonimus",
#       "tk_id":"6a16bdaea300029da9e85cf6c5122589"
#    },
#    "animalia.platyhelminthes.cestoda.taenia":{
#       "path":"animalia.platyhelminthes.cestoda.taenia",
#       "label":"Taenia",
#       "tk_id":"38185776eacde5f2bf34bb45325d2001"
#    },
#    "animalia.platyhelminthes.cestoda.taenia_saginata":{
#       "path":"animalia.platyhelminthes.cestoda.taenia_saginata",
#       "label":"Taenia_saginata",
#       "tk_id":"38185776eacde5f2bf34bb45325d2001"
#    },
#    "animalia.mollusca.gastropoda.nudibranch":{
#       "path":"animalia.mollusca.gastropoda.nudibranch",
#       "label":"Nudibranch",
#       "tk_id":"c5a3265f2ef40ab72d1a22cc255d567f"
#    },
#    "animalia.mollusca.gastropoda.apple_snails":{
#       "path":"animalia.mollusca.gastropoda.apple_snails",
#       "label":"Apple_snails",
#       "tk_id":"c5a3265f2ef40ab72d1a22cc255d567f"
#    },
#    "animalia.mollusca.cephalopoda.octopus":{
#       "path":"animalia.mollusca.cephalopoda.octopus",
#       "label":"Octopus",
#       "tk_id":"8870e0171cbf60adbe686b860066f495"
#    },
#    "animalia.mollusca.cephalopoda.squid":{
#       "path":"animalia.mollusca.cephalopoda.squid",
#       "label":"Squid",
#       "tk_id":"8870e0171cbf60adbe686b860066f495"
#    },
#    "animalia.echinodermata.asteroidea.choriaster":{
#       "path":"animalia.echinodermata.asteroidea.choriaster",
#       "label":"Choriaster",
#       "tk_id":"3833e77441f77669da3b9ccac442ec54"
#    },
#    "animalia.echinodermata.asteroidea.valvatida":{
#       "path":"animalia.echinodermata.asteroidea.valvatida",
#       "label":"Valvatida",
#       "tk_id":"3833e77441f77669da3b9ccac442ec54"
#    },
#    "animalia.echinodermata.ophiuroidea.basket_stars":{
#       "path":"animalia.echinodermata.ophiuroidea.basket_stars",
#       "label":"Basket_stars",
#       "tk_id":"db89407aef4ec4b646f09269d373261e"
#    },
#    "animalia.echinodermata.ophiuroidea.ophiurida":{
#       "path":"animalia.echinodermata.ophiuroidea.ophiurida",
#       "label":"Ophiurida",
#       "tk_id":"db89407aef4ec4b646f09269d373261e"
#    },
#    "animalia.echinodermata.echinoidea.sand_dollar":{
#       "path":"animalia.echinodermata.echinoidea.sand_dollar",
#       "label":"Sand_dollar",
#       "tk_id":"5b8fe0375ad0c0fe2a928026846aeca2"
#    },
#    "animalia.echinodermata.echinoidea.echinoida":{
#       "path":"animalia.echinodermata.echinoidea.echinoida",
#       "label":"Echinoida",
#       "tk_id":"5b8fe0375ad0c0fe2a928026846aeca2"
#    }
# }
#
