<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 全量获取file元信息的请求body
 */
class ScanFileMetaRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'category' => 'category',
        'driveId' => 'drive_id',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess' => 'image_thumbnail_process',
        'imageUrlProcess' => 'image_url_process',
        'limit' => 'limit',
        'marker' => 'marker',
        'videoThumbnailProcess' => 'video_thumbnail_process',
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('limit', $this->limit, 5000);
        Model::validateMinimum('limit', $this->limit, 1);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->category) {
            $res['category'] = $this->category;
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
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ScanFileMetaRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['category'])){
            $model->category = $map['category'];
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
        if(isset($map['marker'])){
            $model->marker = $map['marker'];
        }
        if(isset($map['video_thumbnail_process'])){
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description category
     * @example image
     * @var string
     */
    public $category;

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
     * @example 1000
     * @var int
     */
    public $limit;

    /**
     * @description marker
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     * @var string
     */
    public $marker;

    /**
     * @description video_thumbnail_process
type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     * @var string
     */
    public $videoThumbnailProcess;

}
