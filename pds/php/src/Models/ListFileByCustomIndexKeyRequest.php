<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 列举文件.
 */
class ListFileByCustomIndexKeyRequest extends Model
{
    public $headers;

    /**
     * @description starred
     *
     * @example false
     *
     * @var bool
     */
    public $Starred;

    /**
     * @description addition_data
     *
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description category
     *
     * @example image
     *
     * @var string
     */
    public $category;

    /**
     * @description custom_index_key
     *
     * @var string
     */
    public $customIndexKey;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description encrypt_mode
     *
     * @var string
     */
    public $encryptMode;

    /**
     * @description fields
     *
     * @example *
     *
     * @var string
     */
    public $fields;

    /**
     * @example 1:1, 1:2, 2:1, 2:3, 3:2, 7:4
     *
     * @var string[]
     */
    public $imageCroppingAspectRatios;

    /**
     * @description image_thumbnail_process
     *
     * @example image/resize,w_200
     *
     * @var string
     */
    public $imageThumbnailProcess;

    /**
     * @description image_url_process
     *
     * @example image/resize,w_200
     *
     * @var string
     */
    public $imageUrlProcess;

    /**
     * @description limit
     *
     * @example 10
     *
     * @var int
     */
    public $limit;

    /**
     * @description marker
     *
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     *
     * @var string
     */
    public $marker;

    /**
     * @description order_direction
     *
     * @example ASC
     *
     * @var string
     */
    public $orderDirection;

    /**
     * @var string
     */
    public $referer;

    /**
     * @description share_id, either share_id or drive_id is required
     *
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     *
     * @var string
     */
    public $shareId;

    /**
     * @var string
     */
    public $signToken;

    /**
     * @description status
     *
     * @example available
     *
     * @var string
     */
    public $status;

    /**
     * @description type
     *
     * @example file
     *
     * @var string
     */
    public $type;

    /**
     * @description url_expire_sec
     *
     * @example 900
     *
     * @var int
     */
    public $urlExpireSec;

    /**
     * @description video_thumbnail_process
     * type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     *
     * @var string
     */
    public $videoThumbnailProcess;
    protected $_name = [
        'Starred'                   => 'Starred',
        'additionData'              => 'addition_data',
        'category'                  => 'category',
        'customIndexKey'            => 'custom_index_key',
        'driveId'                   => 'drive_id',
        'encryptMode'               => 'encrypt_mode',
        'fields'                    => 'fields',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess'     => 'image_thumbnail_process',
        'imageUrlProcess'           => 'image_url_process',
        'limit'                     => 'limit',
        'marker'                    => 'marker',
        'orderDirection'            => 'order_direction',
        'referer'                   => 'referer',
        'shareId'                   => 'share_id',
        'signToken'                 => 'sign_token',
        'status'                    => 'status',
        'type'                      => 'type',
        'urlExpireSec'              => 'url_expire_sec',
        'videoThumbnailProcess'     => 'video_thumbnail_process',
    ];
    protected $_default = [
        'limit'        => 50,
        'status'       => 'available',
        'urlExpireSec' => 900,
    ];

    public function validate()
    {
        Model::validateRequired('customIndexKey', $this->customIndexKey, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMaximum('urlExpireSec', $this->urlExpireSec, 14400);
        Model::validateMinimum('limit', $this->limit, 0);
        Model::validateMinimum('urlExpireSec', $this->urlExpireSec, 10);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->Starred) {
            $res['Starred'] = $this->Starred;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->category) {
            $res['category'] = $this->category;
        }
        if (null !== $this->customIndexKey) {
            $res['custom_index_key'] = $this->customIndexKey;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->fields) {
            $res['fields'] = $this->fields;
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
        if (null !== $this->orderDirection) {
            $res['order_direction'] = $this->orderDirection;
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
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
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
     *
     * @return ListFileByCustomIndexKeyRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['Starred'])) {
            $model->Starred = $map['Starred'];
        }
        if (isset($map['addition_data'])) {
            $model->additionData = $map['addition_data'];
        }
        if (isset($map['category'])) {
            $model->category = $map['category'];
        }
        if (isset($map['custom_index_key'])) {
            $model->customIndexKey = $map['custom_index_key'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['encrypt_mode'])) {
            $model->encryptMode = $map['encrypt_mode'];
        }
        if (isset($map['fields'])) {
            $model->fields = $map['fields'];
        }
        if (isset($map['image_cropping_aspect_ratios'])) {
            if (!empty($map['image_cropping_aspect_ratios'])) {
                $model->imageCroppingAspectRatios = $map['image_cropping_aspect_ratios'];
            }
        }
        if (isset($map['image_thumbnail_process'])) {
            $model->imageThumbnailProcess = $map['image_thumbnail_process'];
        }
        if (isset($map['image_url_process'])) {
            $model->imageUrlProcess = $map['image_url_process'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }
        if (isset($map['order_direction'])) {
            $model->orderDirection = $map['order_direction'];
        }
        if (isset($map['referer'])) {
            $model->referer = $map['referer'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['sign_token'])) {
            $model->signToken = $map['sign_token'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }
        if (isset($map['url_expire_sec'])) {
            $model->urlExpireSec = $map['url_expire_sec'];
        }
        if (isset($map['video_thumbnail_process'])) {
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }

        return $model;
    }
}
