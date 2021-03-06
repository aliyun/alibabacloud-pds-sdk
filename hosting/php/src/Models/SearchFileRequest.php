<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 搜索文件元数据
 */
class SearchFileRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId' => 'drive_id',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess' => 'image_thumbnail_process',
        'imageUrlProcess' => 'image_url_process',
        'limit' => 'limit',
        'location' => 'location',
        'marker' => 'marker',
        'orderBy' => 'order_by',
        'query' => 'query',
        'referer' => 'referer',
        'returnTotalCount' => 'return_total_count',
        'signToken' => 'sign_token',
        'urlExpireSec' => 'url_expire_sec',
        'videoThumbnailProcess' => 'video_thumbnail_process',
    ];
    protected $_default = [
        'limit' => 50,
        'orderBy' => 'updated_at',
        'urlExpireSec' => 900,
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMaximum('urlExpireSec', $this->urlExpireSec, 14400);
        Model::validateMinimum('limit', $this->limit, 1);
        Model::validateMinimum('urlExpireSec', $this->urlExpireSec, 10);
        Model::validateMaxLength('query', $this->query, 4096);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->imageCroppingAspectRatios) {
            $res['image_cropping_aspect_ratios'] = $this->imageCroppingAspectRatios;
        }
        if (null !== $this->imageThumbnailProcess) {
            $res['image_thumbnail_process'] = $this->imageThumbnailProcess;
        }
        if (null !== $this->imageUrlProcess) {
            $res['image_url_process'] = $this->imageUrlProcess;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->orderBy) {
            $res['order_by'] = $this->orderBy;
        }
        if (null !== $this->query) {
            $res['query'] = $this->query;
        }
        if (null !== $this->referer) {
            $res['referer'] = $this->referer;
        }
        if (null !== $this->returnTotalCount) {
            $res['return_total_count'] = $this->returnTotalCount;
        }
        if (null !== $this->signToken) {
            $res['sign_token'] = $this->signToken;
        }
        if (null !== $this->urlExpireSec) {
            $res['url_expire_sec'] = $this->urlExpireSec;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return SearchFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['image_cropping_aspect_ratios'])){
            if(!empty($map['image_cropping_aspect_ratios'])){
                $model->imageCroppingAspectRatios = $map['image_cropping_aspect_ratios'];
            }
        }
        if(isset($map['image_thumbnail_process'])){
            $model->imageThumbnailProcess = $map['image_thumbnail_process'];
        }
        if(isset($map['image_url_process'])){
            $model->imageUrlProcess = $map['image_url_process'];
        }
        if(isset($map['limit'])){
            $model->limit = $map['limit'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        if(isset($map['marker'])){
            $model->marker = $map['marker'];
        }
        if(isset($map['order_by'])){
            $model->orderBy = $map['order_by'];
        }
        if(isset($map['query'])){
            $model->query = $map['query'];
        }
        if(isset($map['referer'])){
            $model->referer = $map['referer'];
        }
        if(isset($map['return_total_count'])){
            $model->returnTotalCount = $map['return_total_count'];
        }
        if(isset($map['sign_token'])){
            $model->signToken = $map['sign_token'];
        }
        if(isset($map['url_expire_sec'])){
            $model->urlExpireSec = $map['url_expire_sec'];
        }
        if(isset($map['video_thumbnail_process'])){
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }
        return $model;
    }
    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @example 1:1, 1:2, 2:1, 2:3, 3:2, 7:4
     * @var string[]
     */
    public $imageCroppingAspectRatios;

    /**
     * @description image_thumbnail_process
     * @example image/resize,w_200
     * @var string
     */
    public $imageThumbnailProcess;

    /**
     * @description image_url_process
     * @example image/resize,w_200
     * @var string
     */
    public $imageUrlProcess;

    /**
     * @description limit
     * @example 10
     * @var int
     */
    public $limit;

    /**
     * @description location
     * @example cn-hangzhou
     * @var string
     */
    public $location;

    /**
     * @description Marker
     * @example ""
     * @var string
     */
    public $marker;

    /**
     * @description order_by
     * @example size
     * @var string
     */
    public $orderBy;

    /**
     * @description query
     * @example not name=123
     * @var string
     */
    public $query;

    /**
     * @description referer
     * @var string
     */
    public $referer;

    /**
     * @description return_total_count 是否返回查询总数
     * @var bool
     */
    public $returnTotalCount;

    /**
     * @description sign_token
     * @var string
     */
    public $signToken;

    /**
     * @description url_expire_sec
     * @example 900
     * @var int
     */
    public $urlExpireSec;

    /**
     * @description video_thumbnail_process
type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     * @var string
     */
    public $videoThumbnailProcess;

}
