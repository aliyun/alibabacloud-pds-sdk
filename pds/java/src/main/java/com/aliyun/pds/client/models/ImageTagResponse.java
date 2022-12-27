// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageTagResponse extends TeaModel {
    /**
     * <p>聚类标签计数</p>
     */
    @NameInMap("count")
    public Long count;

    /**
     * <p>cover_file_category</p>
     */
    @NameInMap("cover_file_category")
    public String coverFileCategory;

    /**
     * <p>cover_file_id</p>
     */
    @NameInMap("cover_file_id")
    public String coverFileId;

    /**
     * <p>cover_score</p>
     */
    @NameInMap("cover_overall_score")
    public Double coverOverallScore;

    /**
     * <p>cover_tag_confidence</p>
     */
    @NameInMap("cover_tag_confidence")
    public Double coverTagConfidence;

    /**
     * <p>聚类标签封面图片地址</p>
     */
    @NameInMap("cover_url")
    public String coverUrl;

    /**
     * <p>聚类标签名称</p>
     */
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

    public ImageTagResponse setCoverFileCategory(String coverFileCategory) {
        this.coverFileCategory = coverFileCategory;
        return this;
    }
    public String getCoverFileCategory() {
        return this.coverFileCategory;
    }

    public ImageTagResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public ImageTagResponse setCoverOverallScore(Double coverOverallScore) {
        this.coverOverallScore = coverOverallScore;
        return this;
    }
    public Double getCoverOverallScore() {
        return this.coverOverallScore;
    }

    public ImageTagResponse setCoverTagConfidence(Double coverTagConfidence) {
        this.coverTagConfidence = coverTagConfidence;
        return this;
    }
    public Double getCoverTagConfidence() {
        return this.coverTagConfidence;
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
