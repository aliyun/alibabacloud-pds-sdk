<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取文件元数据
 */
class GetFileRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId' => 'drive_id',
        'fields' => 'fields',
        'fileId' => 'file_id',
        'fileIdPath' => 'file_id_path',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess' => 'image_thumbnail_process',
        'imageUrlProcess' => 'image_url_process',
        'location' => 'location',
        'referer' => 'referer',
        'shareId' => 'share_id',
        'signToken' => 'sign_token',
        'urlExpireSec' => 'url_expire_sec',
        'videoThumbnailProcess' => 'video_thumbnail_process',
    ];
    protected $_default = [
        'fields' => '*',
        'urlExpireSec' => 900,
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMaximum('urlExpireSec', $this->urlExpireSec, 14400);
        Model::validateMinimum('urlExpireSec', $this->urlExpireSec, 10);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fields) {
            $res['fields'] = $this->fields;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileIdPath) {
            $res['file_id_path'] = $this->fileIdPath;
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
        if (null !== $this->location) {
            $res['location'] = $this->location;
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
     * @return GetFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['fields'])){
            $model->fields = $map['fields'];
        }
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['file_id_path'])){
            $model->fileIdPath = $map['file_id_path'];
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
        if(isset($map['location'])){
            $model->location = $map['location'];
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
        if(isset($map['url_expire_sec'])){
            $model->urlExpireSec = $map['url_expire_sec'];
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
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description fields
     * @example *
     * @var string
     */
    public $fields;

    /**
     * @description file_id
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     * @var string
     */
    public $fileId;

    /**
     * @var string
     */
    public $fileIdPath;

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
     * @description location
     * @example cn-hangzhou
     * @var string
     */
    public $location;

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
