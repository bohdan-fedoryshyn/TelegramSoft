package com.Rpg.repository;

import com.Rpg.entity.Account;
import com.Rpg.entity.Status;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface AccountRepository extends JpaRepository<Account ,Long> {

    List<Account> getAccountByStatus(Status status);

}

