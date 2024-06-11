package com.creative.todoApi.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.ConfigurableEnvironment;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;

@Configuration
@RequiredArgsConstructor
public class DataSourceConfig {

    private final ConfigurableEnvironment environment;

    @Bean
    public DataSource dataSource() {
        return getDataSource();
    }

    private DriverManagerDataSource getDataSource() {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl(environment.getProperty("jdbc.mysql.datasource.url"));
        dataSource.setUsername(environment.getProperty("jdbc.mysql.datasource.username"));
        dataSource.setPassword(environment.getProperty("jdbc.mysql.datasource.password"));
        return dataSource;
    }
}