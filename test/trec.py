from torchtext import data
from torchtext import datasets


# Approach 1:
# set up fields
TEXT = data.Field(lower=True, include_lengths=True, batch_first=True)
LABEL = data.Field(sequential=False)


# make splits for data
train, test = datasets.TREC.splits(TEXT, LABEL, fine_grained=True)

# print information about the data
print('train.fields', train.fields)
print('len(train)', len(train))
print('vars(train[0])', vars(train[0]))

# build the vocabulary

TEXT.build_vocab(train, vectors='glove.6B.300d')
LABEL.build_vocab(train)

# print vocab information
print('len(TEXT.vocab)', len(TEXT.vocab))
print('TEXT.vocab.vectors.size()', TEXT.vocab.vectors.size())

# make iterator for splits
train_iter, test_iter = data.BucketIterator.splits(
    (train, test), batch_size=3, device=0)

# print batch information
batch = next(iter(train_iter))
print(batch.text)
print(batch.label)

# Approach 2:
TEXT.build_vocab(train, vectors=['glove.840B.300d', 'charngram.100d'])
LABEL.build_vocab(train)

train_iter, test_iter = datasets.TREC.iters(batch_size=4)

# print batch information
batch = next(iter(train_iter))
print(batch.text)
print(batch.label)
