// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * user_tags 字段
 */
public class BaseUserTagsRequest extends TeaModel {
    /**
     * <p>user_tags</p>
     */
    @NameInMap("user_tags")
    public java.util.List<UserTag> userTags;

    public static BaseUserTagsRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseUserTagsRequest self = new BaseUserTagsRequest();
        return TeaModel.build(map, self);
    }

    public BaseUserTagsRequest setUserTags(java.util.List<UserTag> userTags) {
        this.userTags = userTags;
        return this;
    }
    public java.util.List<UserTag> getUserTags() {
        return this.userTags;
    }

}
