// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * request
 */
public class DeletePermissionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("collection")
    public String collection;

    @NameInMap("identity_id")
    public String identityId;

    @NameInMap("identity_type")
    public String identityType;

    @NameInMap("resource")
    public String resource;

    @NameInMap("resource_type")
    public String resourceType;

    public static DeletePermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        DeletePermissionRequest self = new DeletePermissionRequest();
        return TeaModel.build(map, self);
    }

    public DeletePermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public DeletePermissionRequest setCollection(String collection) {
        this.collection = collection;
        return this;
    }
    public String getCollection() {
        return this.collection;
    }

    public DeletePermissionRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public DeletePermissionRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public DeletePermissionRequest setResource(String resource) {
        this.resource = resource;
        return this;
    }
    public String getResource() {
        return this.resource;
    }

    public DeletePermissionRequest setResourceType(String resourceType) {
        this.resourceType = resourceType;
        return this;
    }
    public String getResourceType() {
        return this.resourceType;
    }

}
