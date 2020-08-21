// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageTagResponse extends TeaModel {
    // 聚类标签计数
    @NameInMap("count")
    public Long count;

    // cover_file_id
    @NameInMap("cover_file_id")
    public String coverFileId;

    // 聚类标签封面图片地址
    @NameInMap("cover_url")
    public String coverUrl;

    // 聚类标签名称
    @NameInMap("name")
    public String name;

    public static ImageTagResponse build(java.util.Map<String, ?> map) throws Exception {
        ImageTagResponse self = new ImageTagResponse();
        return TeaModel.build(map, self);
    }

    public ImageTagResponse setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public ImageTagResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public ImageTagResponse setCoverUrl(String coverUrl) {
        this.coverUrl = coverUrl;
        return this;
    }
    public String getCoverUrl() {
        return this.coverUrl;
    }

    public ImageTagResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
