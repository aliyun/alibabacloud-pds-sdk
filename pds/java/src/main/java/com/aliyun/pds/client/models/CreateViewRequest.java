// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Create view request
 */
public class CreateViewRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // category
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    // description
    @NameInMap("description")
    public String description;

    // name
    @NameInMap("name")
    @Validation(required = true)
    public String name;

    // owner
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    // user_id
    @NameInMap("user_id")
    public String userId;

    public static CreateViewRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateViewRequest self = new CreateViewRequest();
        return TeaModel.build(map, self);
    }

    public CreateViewRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateViewRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CreateViewRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateViewRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public CreateViewRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public CreateViewRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
