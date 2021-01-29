<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list file request
 */
class BaseListFileRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId' => 'drive_id',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess' => 'image_thumbnail_process',
        'imageUrlProcess' => 'image_url_process',
        'limit' => 'limit',
        'marker' => 'marker',
        'referer' => 'referer',
        'shareId' => 'share_id',
        'signToken' => 'sign_token',
        'videoThumbnailProcess' => 'video_thumbnail_process',
    ];
    protected $_default = [
        'limit' => 50,
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMinimum('limit', $this->limit, 0);
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
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->referer) {
            $res['referer'] = $this->referer;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->signToken) {
            $res['sign_token'] = $this->signToken;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return BaseListFileRequest
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
        if(isset($map['marker'])){
            $model->marker = $map['marker'];
        }
        if(isset($map['referer'])){
            $model->referer = $map['referer'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['sign_token'])){
            $model->signToken = $map['sign_token'];
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
     * @description marker
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     * @var string
     */
    public $marker;

    /**
     * @var string
     */
    public $referer;

    /**
     * @description share_id, either share_id or drive_id is required
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     * @var string
     */
    public $shareId;

    /**
     * @var string
     */
    public $signToken;

    /**
     * @description video_thumbnail_process
type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     * @var string
     */
    public $videoThumbnailProcess;

}
