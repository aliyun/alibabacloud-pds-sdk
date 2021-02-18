<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\BaseCCPFileResponse;

/**
 * 故事详情
 */
class GetStoryDetailResponse extends Model {
    protected $_name = [
        'coverFileId' => 'cover_file_id',
        'createdAt' => 'created_at',
        'items' => 'items',
        'score' => 'score',
        'storyId' => 'story_id',
        'storyImagesDateRange' => 'story_images_date_range',
        'subTitle' => 'sub_title',
        'title' => 'title',
        'updatedAt' => 'updated_at',
        'videoStatus' => 'video_status',
        'videoUrl' => 'video_url',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->coverFileId) {
            $res['cover_file_id'] = $this->coverFileId;
        }
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->items) {
            $res['items'] = [];
            if(null !== $this->items && is_array($this->items)){
                $n = 0;
                foreach($this->items as $item){
                    $res['items'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->score) {
            $res['score'] = $this->score;
        }
        if (null !== $this->storyId) {
            $res['story_id'] = $this->storyId;
        }
        if (null !== $this->storyImagesDateRange) {
            $res['story_images_date_range'] = $this->storyImagesDateRange;
        }
        if (null !== $this->subTitle) {
            $res['sub_title'] = $this->subTitle;
        }
        if (null !== $this->title) {
            $res['title'] = $this->title;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }
        if (null !== $this->videoStatus) {
            $res['video_status'] = $this->videoStatus;
        }
        if (null !== $this->videoUrl) {
            $res['video_url'] = $this->videoUrl;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetStoryDetailResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['cover_file_id'])){
            $model->coverFileId = $map['cover_file_id'];
        }
        if(isset($map['created_at'])){
            $model->createdAt = $map['created_at'];
        }
        if(isset($map['items'])){
            if(!empty($map['items'])){
                $model->items = [];
                $n = 0;
                foreach($map['items'] as $item) {
                    $model->items[$n++] = null !== $item ? BaseCCPFileResponse::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['score'])){
            $model->score = $map['score'];
        }
        if(isset($map['story_id'])){
            $model->storyId = $map['story_id'];
        }
        if(isset($map['story_images_date_range'])){
            if(!empty($map['story_images_date_range'])){
                $model->storyImagesDateRange = $map['story_images_date_range'];
            }
        }
        if(isset($map['sub_title'])){
            $model->subTitle = $map['sub_title'];
        }
        if(isset($map['title'])){
            $model->title = $map['title'];
        }
        if(isset($map['updated_at'])){
            $model->updatedAt = $map['updated_at'];
        }
        if(isset($map['video_status'])){
            $model->videoStatus = $map['video_status'];
        }
        if(isset($map['video_url'])){
            $model->videoUrl = $map['video_url'];
        }
        return $model;
    }
    /**
     * @description cover_file_id
     * @var string
     */
    public $coverFileId;

    /**
     * @description created_at
     * @var string
     */
    public $createdAt;

    /**
     * @description items
     * @var BaseCCPFileResponse[]
     */
    public $items;

    /**
     * @description score
     * @example 50.5
     * @var float
     */
    public $score;

    /**
     * @description story_id
     * @example "abc"
     * @var string
     */
    public $storyId;

    /**
     * @description story_images_date_range
     * @var int[]
     */
    public $storyImagesDateRange;

    /**
     * @description sub_title
     * @example "2020"
     * @var string
     */
    public $subTitle;

    /**
     * @description title
     * @example "历史的今天"
     * @var string
     */
    public $title;

    /**
     * @description updated_at
     * @var string
     */
    public $updatedAt;

    /**
     * @description video_status
     * @var string
     */
    public $videoStatus;

    /**
     * @description video_url
     * @example "https://abc.xxx"
     * @var string
     */
    public $videoUrl;

}
