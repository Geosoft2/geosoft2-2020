# First install TileDb if not already done so
# You will need at least R 4.x.x and Rtools40!
# install.packages('tiledb')
library(tiledb)

# Dimensions are created. Most of these objects are tiledb specific classes.
dim1   <- tiledb_dim("dim1", c(1L, 4L), 2L, "INT32")
dim2   <- tiledb_dim("dim2", c(1L, 4L), 2L, "INT32")

# The dimensions are combined into a domain object
dom    <- tiledb_domain(dims = c(dim1,dim2))

# Attribute creation
attr <- tiledb_attr("attr", type = "INT32")
attr2 <- tiledb_attr("attr2", type = "INT32")

# Schema and array Creation
sch    <- tiledb_array_schema(dom, c(attr, attr2), cell_order = "COL_MAJOR",tile_order = "ROW_MAJOR")
tiledb_array_create("demo3", sch)


# Prepare two 4x3 dense array
data <-  array(c(1L, 4L, 2L, 5L, 3L, 6L), dim=c(2,3))
data2 <-  array(c(1L, 1L, 1L, 1L, 1L, 1L), dim=c(2,3))

# Prepare the [1,2] x [2,4] subarray to write to
I <- c(1:2)
J <- c(2:4)

# Open the array and write the data to it and show schema
A <- tiledb_dense(uri = "demo3")
schema(A)
A[I, J] <- list(data, data2)

show(A[I,J])

# Write single cell
A[1,2] <- list(array(c(100L),dim = c(1:1)),array(c(100L),dim = c(1:1)))

show(A[I,J])

# Close array
tiledb_array_close(A)
