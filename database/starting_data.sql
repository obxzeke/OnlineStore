INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `is_admin`)
VALUES ('admin', '2c6d096c92b3571068ca814db6ca92d0ac2e8b079d750a2e78b59cb37da0ee832ff7fea65787d3e645f6733cd04e32a528bf203f691e3dbdccd1582f668d0bc1', 'admin@admin.com', 'admin', 'admin', 1);

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `is_admin`)
Values ('test', 'ce69f4d09c0781eed0b2ef4b647388cbe94c17e0324841b7de3420605a1794371ab9269ca9c1c7d63555c964822ffd1aa49278b81731cfc91693b9085ba45e7d', 'test@test.com', 'test', 'test', 0);

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Apples', 'An edible cultivation of the Malus genus.', 2.00, 100, 'static/images/apple.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Bananas', 'A long curved fruit which grows in clusters and has soft pulpy flesh and yellow skin when ripe.', 1.00, 100, 'static/images/banana.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Mangos', 'The best fruit on the planet.', 4.00, 100, 'static/images/mango.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Oranges', "Hey, they're orange", 4.00, 100, 'static/images/orange.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Acai', "It starts with A", 4.00, 100, 'static/images/acai.jpg', 'Fruit');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, 'sale_rating', 'sale_review', `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30',  3, 'mid at best', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, 'sale_rating', 'sale_review', `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5, 'its like it was made for my hand', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, 'sale_rating', 'sale_review', `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 1, 'the worst fruit on the planet', 5.50);
