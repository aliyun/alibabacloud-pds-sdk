// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * get_share_link_by_anonymous response
 */
public class GetShareLinkByAnonymousResponse extends TeaModel {
    // creator_id
    @NameInMap("creator_id")
    public String creatorId;

    // creator_name
    @NameInMap("creator_name")
    public String creatorName;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    public static GetShareLinkByAnonymousResponse build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkByAnonymousResponse self = new GetShareLinkByAnonymousResponse();
        return TeaModel.build(map, self);
    }

    public GetShareLinkByAnonymousResponse setCreatorId(String creatorId) {
        this.creatorId = creatorId;
        return this;
    }
    public String getCreatorId() {
        return this.creatorId;
    }

    public GetShareLinkByAnonymousResponse setCreatorName(String creatorName) {
        this.creatorName = creatorName;
        return this;
    }
    public String getCreatorName() {
        return this.creatorName;
    }

    public GetShareLinkByAnonymousResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public GetShareLinkByAnonymousResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
